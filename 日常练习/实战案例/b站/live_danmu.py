# -*- coding: utf-8 -*-
import asyncio
import http.cookies
import random
from typing import *

import aiohttp


from client.web import BLiveClient
from tool import web_models

# 直播间ID的取值看直播间URL
from 日常练习.实战案例.b站.client.common import BaseHandler

TEST_ROOM_IDS = [
    55,
]

# 这里填一个已登录账号的cookie的SESSDATA字段的值。不填也可以连接，但是收到弹幕的用户名会打码，UID会变成0
SESSDATA = '2b42da1e%2C1754984809%2C2b9bc%2A21CjBtWVyPrEc2E0XvFMLfKSV69rGnnm5EaD_4ZeWA6ficmP_GflzAwi0hf4DpWZFBCXESVllkTUlKOU5LZXlJRHpIb2Y5ZkhlTERLdVF0QVllNkxoaGJRRnZmdVI2d1N6X0w5MlhpTlpoOVlRdGk1cHFMaHF1dW9fVXhzekkzZWNubmhTdTFsb2ZnIIEC'

session: Optional[aiohttp.ClientSession] = None


async def main():
    init_session()
    try:
        # await run_single_client()
        await run_multi_clients()
    finally:
        await session.close()


def init_session():
    cookies = http.cookies.SimpleCookie()
    cookies['SESSDATA'] = SESSDATA
    cookies['buvid3'] = '15302FD7-5574-8583-FAC9-514D9EF9839F75916infoc'
    cookies['SESSDATA']['domain'] = 'bilibili.com'

    global session
    session = aiohttp.ClientSession()
    session.cookie_jar.update_cookies(cookies)


async def run_single_client():
    """
    演示监听一个直播间
    """
    room_id = random.choice(TEST_ROOM_IDS)
    client = BLiveClient(room_id=room_id, session=session)
    handler = MyHandler()
    client.set_handler(handler)

    client.start()
    try:
        # 演示5秒后停止
        # await asyncio.sleep(5)
        # client.stop()

        await client.join()
    finally:
        await client.stop_and_close()


async def run_multi_clients():
    """
    演示同时监听多个直播间
    """
    clients = [BLiveClient(room_id, session=session) for room_id in TEST_ROOM_IDS]
    handler = MyHandler()
    for client in clients:
        client.set_handler(handler)
        client.start()

    try:
        await asyncio.gather(*(
            client.join() for client in clients
        ))
    finally:
        await asyncio.gather(*(
            client.stop_and_close() for client in clients
        ))


class MyHandler(BaseHandler):
    # # 演示如何添加自定义回调
    # _CMD_CALLBACK_DICT = blivedm.BaseHandler._CMD_CALLBACK_DICT.copy()
    #
    # # 看过数消息回调
    # def __watched_change_callback(self, client: blivedm.BLiveClient, command: dict):
    #     print(f'[{client.room_id}] WATCHED_CHANGE: {command}')
    # _CMD_CALLBACK_DICT['WATCHED_CHANGE'] = __watched_change_callback  # noqa

    def _on_heartbeat(self, client: BLiveClient, message: web_models.HeartbeatMessage):
        print(f'[{client.room_id}] 心跳')

    def _on_danmaku(self, client: BLiveClient, message: web_models.DanmakuMessage):
        print(f'[{client.room_id}] {message.uname}：{message.msg}')

    def _on_gift(self, client: BLiveClient, message: web_models.GiftMessage):
        print(f'[{client.room_id}] {message.uname} 赠送{message.gift_name}x{message.num}'
              f' （{message.coin_type}瓜子x{message.total_coin}）')

    def _on_buy_guard(self, client: BLiveClient, message: web_models.GuardBuyMessage):
        print(f'[{client.room_id}] {message.username} 上舰，guard_level={message.guard_level}')

    def _on_user_toast_v2(self, client: BLiveClient, message: web_models.UserToastV2Message):
        print(f'[{client.room_id}] {message.username} 上舰，guard_level={message.guard_level}')

    def _on_super_chat(self, client: BLiveClient, message: web_models.SuperChatMessage):
        print(f'[{client.room_id}] 醒目留言 ¥{message.price} {message.uname}：{message.message}')

    def _on_interact_word(self, client: BLiveClient, message: web_models.InteractWordMessage):
        if message.msg_type == 1:
            print(f'[{client.room_id}] {message.username} 进入房间')


if __name__ == '__main__':
    asyncio.run(main())
