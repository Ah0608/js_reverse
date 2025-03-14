# -*- coding: utf-8 -*-
import asyncio
import enum
import json
import logging
import struct
import zlib
from typing import *

import aiohttp
import brotli

from 日常练习.实战案例.b站.tool import utils
from 日常练习.实战案例.b站.tool import web_models, open_models

logger = logging.getLogger('blivedm')

__all__ = (
    'HandlerInterface',
    'BaseHandler',
)

USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
)

HEADER_STRUCT = struct.Struct('>I2H2I')


class HeaderTuple(NamedTuple):
    pack_len: int
    raw_header_size: int
    ver: int
    operation: int
    seq_id: int


# WS_BODY_PROTOCOL_VERSION
class ProtoVer(enum.IntEnum):
    NORMAL = 0
    HEARTBEAT = 1
    DEFLATE = 2
    BROTLI = 3


# go-common\app\service\main\broadcast\model\operation.go
class Operation(enum.IntEnum):
    HANDSHAKE = 0
    HANDSHAKE_REPLY = 1
    HEARTBEAT = 2
    HEARTBEAT_REPLY = 3
    SEND_MSG = 4
    SEND_MSG_REPLY = 5
    DISCONNECT_REPLY = 6
    AUTH = 7
    AUTH_REPLY = 8
    RAW = 9
    PROTO_READY = 10
    PROTO_FINISH = 11
    CHANGE_ROOM = 12
    CHANGE_ROOM_REPLY = 13
    REGISTER = 14
    REGISTER_REPLY = 15
    UNREGISTER = 16
    UNREGISTER_REPLY = 17
    # B站业务自定义OP
    # MinBusinessOp = 1000
    # MaxBusinessOp = 10000


# WS_AUTH
class AuthReplyCode(enum.IntEnum):
    OK = 0
    TOKEN_ERROR = -101


class InitError(Exception):
    """初始化失败"""


class AuthError(Exception):
    """认证失败"""


DEFAULT_RECONNECT_POLICY = utils.make_constant_retry_policy(1)


class WebSocketClientBase:
    """
    基于WebSocket的客户端

    :param session: cookie、连接池
    :param heartbeat_interval: 发送心跳包的间隔时间（秒）
    """

    def __init__(
            self,
            session: Optional[aiohttp.ClientSession] = None,
            heartbeat_interval: float = 30,
    ):
        if session is None:
            self._session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10))
            self._own_session = True
        else:
            self._session = session
            self._own_session = False
            assert self._session.loop is asyncio.get_event_loop()  # noqa

        self._heartbeat_interval = heartbeat_interval

        self._need_init_room = True
        self._handler: Optional[HandlerInterface] = None
        """消息处理器"""
        self._get_reconnect_interval: Callable[[int, int], float] = DEFAULT_RECONNECT_POLICY
        """重连间隔时间增长策略"""

        # 在调用init_room后初始化的字段
        self._room_id: Optional[int] = None

        # 在运行时初始化的字段
        self._websocket: Optional[aiohttp.ClientWebSocketResponse] = None
        """WebSocket连接"""
        self._network_future: Optional[asyncio.Future] = None
        """网络协程的future"""
        self._heartbeat_timer_handle: Optional[asyncio.TimerHandle] = None
        """发心跳包定时器的handle"""

    @property
    def is_running(self) -> bool:
        """
        本客户端正在运行，注意调用stop后还没完全停止也算正在运行
        """
        return self._network_future is not None

    @property
    def room_id(self) -> Optional[int]:
        """
        房间ID，调用init_room后初始化
        """
        return self._room_id

    def set_handler(self, handler: Optional['HandlerInterface']):
        """
        设置消息处理器

        注意消息处理器和网络协程运行在同一个协程，如果处理消息耗时太长会阻塞接收消息。如果是CPU密集型的任务，建议将消息推到线程池处理；
        如果是IO密集型的任务，应该使用async函数，并且在handler里使用create_task创建新的协程

        :param handler: 消息处理器
        """
        self._handler = handler

    def set_reconnect_policy(self, get_reconnect_interval: Callable[[int, int], float]):
        """
        设置重连间隔时间增长策略

        :param get_reconnect_interval: 一个可调用对象，输入重试次数 (retry_count, total_retry_count)，返回间隔时间
        """
        self._get_reconnect_interval = get_reconnect_interval

    def start(self):
        """
        启动本客户端
        """
        if self.is_running:
            logger.warning('room=%s client is running, cannot start() again', self.room_id)
            return

        self._network_future = asyncio.create_task(self._network_coroutine_wrapper())

    def stop(self):
        """
        停止本客户端
        """
        if not self.is_running:
            logger.warning('room=%s client is stopped, cannot stop() again', self.room_id)
            return

        self._network_future.cancel()

    async def stop_and_close(self):
        """
        便利函数，停止本客户端并释放本客户端的资源，调用后本客户端将不可用
        """
        if self.is_running:
            self.stop()
            await self.join()
        await self.close()

    async def join(self):
        """
        等待本客户端停止
        """
        if not self.is_running:
            logger.warning('room=%s client is stopped, cannot join()', self.room_id)
            return

        await asyncio.shield(self._network_future)

    async def close(self):
        """
        释放本客户端的资源，调用后本客户端将不可用
        """
        if self.is_running:
            logger.warning('room=%s is calling close(), but client is running', self.room_id)

        # 如果session是自己创建的则关闭session
        if self._own_session:
            await self._session.close()

    async def init_room(self) -> bool:
        """
        初始化连接房间需要的字段

        :return: True代表没有降级，如果需要降级后还可用，重载这个函数返回True
        """
        raise NotImplementedError

    @staticmethod
    def _make_packet(data: Union[dict, str, bytes], operation: int) -> bytes:
        """
        创建一个要发送给服务器的包

        :param data: 包体JSON数据
        :param operation: 操作码，见Operation
        :return: 整个包的数据
        """
        if isinstance(data, dict):
            body = json.dumps(data).encode('utf-8')
        elif isinstance(data, str):
            body = data.encode('utf-8')
        else:
            body = data
        header = HEADER_STRUCT.pack(*HeaderTuple(
            pack_len=HEADER_STRUCT.size + len(body),
            raw_header_size=HEADER_STRUCT.size,
            ver=1,
            operation=operation,
            seq_id=1
        ))
        return header + body

    async def _network_coroutine_wrapper(self):
        """
        负责处理网络协程的异常，网络协程具体逻辑在_network_coroutine里
        """
        exc = None
        try:
            await self._network_coroutine()
        except asyncio.CancelledError:
            # 正常停止
            pass
        except Exception as e:
            logger.exception('room=%s _network_coroutine() finished with exception:', self.room_id)
            exc = e
        finally:
            logger.debug('room=%s _network_coroutine() finished', self.room_id)
            self._network_future = None

        if self._handler is not None:
            self._handler.on_client_stopped(self, exc)

    async def _network_coroutine(self):
        """
        网络协程，负责连接服务器、接收消息、解包
        """
        # retry_count在连接成功后会重置为0，total_retry_count不会
        retry_count = 0
        total_retry_count = 0
        while True:
            try:
                await self._on_before_ws_connect(retry_count)

                # 连接
                async with self._session.ws_connect(
                        self._get_ws_url(retry_count),
                        headers={'User-Agent': utils.USER_AGENT},  # web端的token也会签名UA
                        receive_timeout=self._heartbeat_interval + 5,
                ) as websocket:
                    self._websocket = websocket
                    await self._on_ws_connect()

                    # 处理消息
                    message: aiohttp.WSMessage
                    async for message in websocket:
                        await self._on_ws_message(message)
                        # 至少成功处理1条消息
                        retry_count = 0

            except (aiohttp.ClientConnectionError, asyncio.TimeoutError):
                # 掉线重连
                pass
            except AuthError:
                # 认证失败了，应该重新获取token再重连
                logger.exception('room=%d auth failed, trying init_room() again', self.room_id)
                self._need_init_room = True
            finally:
                self._websocket = None
                await self._on_ws_close()

            # 准备重连
            retry_count += 1
            total_retry_count += 1
            logger.warning(
                'room=%d is reconnecting, retry_count=%d, total_retry_count=%d',
                self.room_id, retry_count, total_retry_count
            )
            await asyncio.sleep(self._get_reconnect_interval(retry_count, total_retry_count))

    async def _on_before_ws_connect(self, retry_count):
        """
        在每次建立连接之前调用，可以用来初始化房间
        """
        if not self._need_init_room:
            return

        if not await self.init_room():
            raise InitError('init_room() failed')
        self._need_init_room = False

    def _get_ws_url(self, retry_count) -> str:
        """
        返回WebSocket连接的URL，可以在这里做故障转移和负载均衡
        """
        raise NotImplementedError

    async def _on_ws_connect(self):
        """
        WebSocket连接成功
        """
        await self._send_auth()
        self._heartbeat_timer_handle = asyncio.get_running_loop().call_later(
            self._heartbeat_interval, self._on_send_heartbeat
        )

    async def _on_ws_close(self):
        """
        WebSocket连接断开
        """
        if self._heartbeat_timer_handle is not None:
            self._heartbeat_timer_handle.cancel()
            self._heartbeat_timer_handle = None

    async def _send_auth(self):
        """
        发送认证包
        """
        raise NotImplementedError

    def _on_send_heartbeat(self):
        """
        定时发送心跳包的回调
        """
        if self._websocket is None or self._websocket.closed:
            self._heartbeat_timer_handle = None
            return

        self._heartbeat_timer_handle = asyncio.get_running_loop().call_later(
            self._heartbeat_interval, self._on_send_heartbeat
        )
        asyncio.create_task(self._send_heartbeat())

    async def _send_heartbeat(self):
        """
        发送心跳包
        """
        if self._websocket is None or self._websocket.closed:
            return

        try:
            await self._websocket.send_bytes(self._make_packet({}, Operation.HEARTBEAT))
        except (ConnectionResetError, aiohttp.ClientConnectionError) as e:
            logger.warning('room=%d _send_heartbeat() failed: %r', self.room_id, e)
        except Exception:  # noqa
            logger.exception('room=%d _send_heartbeat() failed:', self.room_id)

    async def _on_ws_message(self, message: aiohttp.WSMessage):
        """
        收到WebSocket消息

        :param message: WebSocket消息
        """
        if message.type != aiohttp.WSMsgType.BINARY:
            logger.warning('room=%d unknown websocket message type=%s, data=%s', self.room_id,
                           message.type, message.data)
            return

        try:
            await self._parse_ws_message(message.data)
        except AuthError:
            # 认证失败，让外层处理
            raise
        except Exception:  # noqa
            logger.exception('room=%d _parse_ws_message() error:', self.room_id)

    async def _parse_ws_message(self, data: bytes):
        """
        解析WebSocket消息

        :param data: WebSocket消息数据
        """
        offset = 0
        try:
            header = HeaderTuple(*HEADER_STRUCT.unpack_from(data, offset))
        except struct.error:
            logger.exception('room=%d parsing header failed, offset=%d, data=%s', self.room_id, offset, data)
            return

        if header.operation in (Operation.SEND_MSG_REPLY, Operation.AUTH_REPLY):
            # 业务消息，可能有多个包一起发，需要分包
            while True:
                body = data[offset + header.raw_header_size: offset + header.pack_len]
                await self._parse_business_message(header, body)

                offset += header.pack_len
                if offset >= len(data):
                    break

                try:
                    header = HeaderTuple(*HEADER_STRUCT.unpack_from(data, offset))
                except struct.error:
                    logger.exception('room=%d parsing header failed, offset=%d, data=%s', self.room_id, offset, data)
                    break

        elif header.operation == Operation.HEARTBEAT_REPLY:
            # 服务器心跳包，前4字节是人气值，后面是客户端发的心跳包内容
            # pack_len不包括客户端发的心跳包内容，不知道是不是服务器BUG
            body = data[offset + header.raw_header_size: offset + header.raw_header_size + 4]
            popularity = int.from_bytes(body, 'big')
            # 自己造个消息当成业务消息处理
            body = {
                'cmd': '_HEARTBEAT',
                'data': {
                    'popularity': popularity
                }
            }
            self._handle_command(body)

        else:
            # 未知消息
            body = data[offset + header.raw_header_size: offset + header.pack_len]
            logger.warning('room=%d unknown message operation=%d, header=%s, body=%s', self.room_id,
                           header.operation, header, body)

    async def _parse_business_message(self, header: HeaderTuple, body: bytes):
        """
        解析业务消息
        """
        if header.operation == Operation.SEND_MSG_REPLY:
            # 业务消息
            if header.ver == ProtoVer.BROTLI:
                # 压缩过的先解压，为了避免阻塞网络线程，放在其他线程执行
                body = await asyncio.get_running_loop().run_in_executor(None, brotli.decompress, body)
                await self._parse_ws_message(body)
            elif header.ver == ProtoVer.DEFLATE:
                # web端已经不用zlib压缩了，但是开放平台会用
                body = await asyncio.get_running_loop().run_in_executor(None, zlib.decompress, body)
                await self._parse_ws_message(body)
            elif header.ver == ProtoVer.NORMAL:
                # 没压缩过的直接反序列化，因为有万恶的GIL，这里不能并行避免阻塞
                if len(body) != 0:
                    try:
                        body = json.loads(body.decode('utf-8'))
                        self._handle_command(body)
                    except Exception:
                        logger.error('room=%d, body=%s', self.room_id, body)
                        raise
            else:
                # 未知格式
                logger.warning('room=%d unknown protocol version=%d, header=%s, body=%s', self.room_id,
                               header.ver, header, body)

        elif header.operation == Operation.AUTH_REPLY:
            # 认证响应
            body = json.loads(body.decode('utf-8'))
            if body['code'] != AuthReplyCode.OK:
                raise AuthError(f"auth reply error, code={body['code']}, body={body}")
            await self._websocket.send_bytes(self._make_packet({}, Operation.HEARTBEAT))

        else:
            # 未知消息
            logger.warning('room=%d unknown message operation=%d, header=%s, body=%s', self.room_id,
                           header.operation, header, body)

    def _handle_command(self, command: dict):
        """
        处理业务消息

        :param command: 业务消息
        """
        if self._handler is None:
            return
        try:
            # 为什么不做成异步的：
            # 1. 为了保持处理消息的顺序，这里不使用call_soon、create_task等方法延迟处理
            # 2. 如果支持handle使用async函数，用户可能会在里面处理耗时很长的异步操作，导致网络协程阻塞
            # 这里做成同步的，强制用户使用create_task或消息队列处理异步操作，这样就不会阻塞网络协程
            self._handler.handle(self, command)
        except Exception as e:
            logger.exception('room=%d _handle_command() failed, command=%s', self.room_id, command, exc_info=e)


logged_unknown_cmds = {
    'COMBO_SEND',
    'ENTRY_EFFECT',
    'HOT_RANK_CHANGED',
    'HOT_RANK_CHANGED_V2',
    'LIVE',
    'LIVE_INTERACTIVE_GAME',
    'NOTICE_MSG',
    'ONLINE_RANK_COUNT',
    'ONLINE_RANK_TOP3',
    'ONLINE_RANK_V2',
    'PK_BATTLE_END',
    'PK_BATTLE_FINAL_PROCESS',
    'PK_BATTLE_PROCESS',
    'PK_BATTLE_PROCESS_NEW',
    'PK_BATTLE_SETTLE',
    'PK_BATTLE_SETTLE_USER',
    'PK_BATTLE_SETTLE_V2',
    'PREPARING',
    'ROOM_REAL_TIME_MESSAGE_UPDATE',
    'STOP_LIVE_ROOM_LIST',
    'SUPER_CHAT_MESSAGE_JPN',
    'USER_TOAST_MSG',
    'WIDGET_BANNER',
}
"""已打日志的未知cmd"""


class HandlerInterface:
    """
    直播消息处理器接口
    """

    def handle(self, client: WebSocketClientBase, command: dict):
        raise NotImplementedError

    def on_client_stopped(self, client: WebSocketClientBase, exception: Optional[Exception]):
        """
        当客户端停止时调用。可以在这里close或者重新start
        """


def _make_msg_callback(method_name, message_cls):
    def callback(self: 'BaseHandler', client: WebSocketClientBase, command: dict):
        method = getattr(self, method_name)
        return method(client, message_cls.from_command(command['data']))

    return callback


class BaseHandler(HandlerInterface):
    """
    一个简单的消息处理器实现，带消息分发和消息类型转换。继承并重写_on_xxx方法即可实现自己的处理器
    """

    def __danmu_msg_callback(self, client: WebSocketClientBase, command: dict):
        return self._on_danmaku(client, web_models.DanmakuMessage.from_command(command['info']))

    _CMD_CALLBACK_DICT: Dict[
        str,
        Optional[Callable[
            ['BaseHandler', WebSocketClientBase, dict],
            Any
        ]]
    ]
    """cmd -> 处理回调"""
    _CMD_CALLBACK_DICT = {
        # 收到心跳包，这是blivedm自造的消息，原本的心跳包格式不一样
        '_HEARTBEAT': _make_msg_callback('_on_heartbeat', web_models.HeartbeatMessage),
        # 弹幕
        # go-common\app\service\live\live-dm\service\v1\send.go
        'DANMU_MSG': __danmu_msg_callback,
        # 礼物
        'SEND_GIFT': _make_msg_callback('_on_gift', web_models.GiftMessage),
        # 上舰
        'GUARD_BUY': _make_msg_callback('_on_buy_guard', web_models.GuardBuyMessage),
        # 另一个上舰消息
        'USER_TOAST_MSG_V2': _make_msg_callback('_on_user_toast_v2', web_models.UserToastV2Message),
        # 醒目留言
        'SUPER_CHAT_MESSAGE': _make_msg_callback('_on_super_chat', web_models.SuperChatMessage),
        # 删除醒目留言
        'SUPER_CHAT_MESSAGE_DELETE': _make_msg_callback('_on_super_chat_delete', web_models.SuperChatDeleteMessage),
        # 进入房间、关注主播等互动消息
        'INTERACT_WORD': _make_msg_callback('_on_interact_word', web_models.InteractWordMessage),

        #
        # 开放平台消息
        #

        # 弹幕
        'LIVE_OPEN_PLATFORM_DM': _make_msg_callback('_on_open_live_danmaku', open_models.DanmakuMessage),
        # 礼物
        'LIVE_OPEN_PLATFORM_SEND_GIFT': _make_msg_callback('_on_open_live_gift', open_models.GiftMessage),
        # 上舰
        'LIVE_OPEN_PLATFORM_GUARD': _make_msg_callback('_on_open_live_buy_guard', open_models.GuardBuyMessage),
        # 醒目留言
        'LIVE_OPEN_PLATFORM_SUPER_CHAT': _make_msg_callback('_on_open_live_super_chat', open_models.SuperChatMessage),
        # 删除醒目留言
        'LIVE_OPEN_PLATFORM_SUPER_CHAT_DEL': _make_msg_callback(
            '_on_open_live_super_chat_delete', open_models.SuperChatDeleteMessage
        ),
        # 点赞
        'LIVE_OPEN_PLATFORM_LIKE': _make_msg_callback('_on_open_live_like', open_models.LikeMessage),
        # 进入房间
        'LIVE_OPEN_PLATFORM_LIVE_ROOM_ENTER': _make_msg_callback('_on_open_live_enter_room',
                                                                 open_models.RoomEnterMessage),
        # 开始直播
        'LIVE_OPEN_PLATFORM_LIVE_START': _make_msg_callback('_on_open_live_start_live', open_models.LiveStartMessage),
        # 结束直播
        'LIVE_OPEN_PLATFORM_LIVE_END': _make_msg_callback('_on_open_live_end_live', open_models.LiveEndMessage),
    }

    def handle(self, client: WebSocketClientBase, command: dict):
        cmd = command.get('cmd', '')
        pos = cmd.find(':')  # 2019-5-29 B站弹幕升级新增了参数
        if pos != -1:
            cmd = cmd[:pos]

        if cmd not in self._CMD_CALLBACK_DICT:
            # 只有第一次遇到未知cmd时打日志
            if cmd not in logged_unknown_cmds:
                logger.warning('room=%d unknown cmd=%s, command=%s', client.room_id, cmd, command)
                logged_unknown_cmds.add(cmd)
            return

        callback = self._CMD_CALLBACK_DICT[cmd]
        if callback is not None:
            callback(self, client, command)

    def _on_heartbeat(self, client: WebSocketClientBase, message: web_models.HeartbeatMessage):
        """收到心跳包"""

    def _on_danmaku(self, client: WebSocketClientBase, message: web_models.DanmakuMessage):
        """弹幕"""

    def _on_gift(self, client: WebSocketClientBase, message: web_models.GiftMessage):
        """礼物"""

    def _on_buy_guard(self, client: WebSocketClientBase, message: web_models.GuardBuyMessage):
        """上舰"""

    def _on_user_toast_v2(self, client: WebSocketClientBase, message: web_models.UserToastV2Message):
        """另一个上舰消息"""

    def _on_super_chat(self, client: WebSocketClientBase, message: web_models.SuperChatMessage):
        """醒目留言"""

    def _on_super_chat_delete(self, client: WebSocketClientBase, message: web_models.SuperChatDeleteMessage):
        """删除醒目留言"""

    def _on_interact_word(self, client: WebSocketClientBase, message: web_models.InteractWordMessage):
        """进入房间、关注主播等互动消息"""

    #
    # 开放平台消息
    #

    def _on_open_live_danmaku(self, client: WebSocketClientBase, message: open_models.DanmakuMessage):
        """弹幕"""

    def _on_open_live_gift(self, client: WebSocketClientBase, message: open_models.GiftMessage):
        """礼物"""

    def _on_open_live_buy_guard(self, client: WebSocketClientBase, message: open_models.GuardBuyMessage):
        """上舰"""

    def _on_open_live_super_chat(self, client: WebSocketClientBase, message: open_models.SuperChatMessage):
        """醒目留言"""

    def _on_open_live_super_chat_delete(
            self, client: WebSocketClientBase, message: open_models.SuperChatDeleteMessage
    ):
        """删除醒目留言"""

    def _on_open_live_like(self, client: WebSocketClientBase, message: open_models.LikeMessage):
        """点赞"""

    def _on_open_live_enter_room(self, client: WebSocketClientBase, message: open_models.RoomEnterMessage):
        """进入房间"""

    def _on_open_live_start_live(self, client: WebSocketClientBase, message: open_models.LiveStartMessage):
        """开始直播"""

    def _on_open_live_end_live(self, client: WebSocketClientBase, message: open_models.LiveEndMessage):
        """结束直播"""
