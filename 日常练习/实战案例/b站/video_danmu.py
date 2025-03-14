import json
import random
from time import sleep

import requests
from loguru import logger
from google.protobuf.json_format import MessageToJson

from 日常练习.实战案例.b站.tool.bili_pb2 import DmSegMobileReply

cookies = {
    'buvid3': '15302FD7-5574-8583-FAC9-514D9EF9839F75916infoc',
    'rpdid': "|(kRk|uRJ|l0J'uYmk|~~k~)",
    'header_theme_version': 'CLOSE',
    'buvid_fp_plain': 'undefined',
    'enable_web_push': 'DISABLE',
    'LIVE_BUVID': 'AUTO8316989143482440',
    'FEED_LIVE_VERSION': 'V_WATCHLATER_PIP_WINDOW3',
    'home_feed_column': '5',
    'CURRENT_QUALITY': '80',
    'buvid4': 'C1DC1876-9A8F-841A-79B7-9DB9E3A406FC40676-023030912-c5iCHVUoavLDhv4Zp%2Br9Gg%3D%3D',
    'b_nut': '100',
    '_uuid': 'CF9101526-EFE8-4BF9-BDE1-11D104F6529CE99975infoc',
    'fingerlogger.info': '4740ab9e6485e28f49f6522cd558bbe9',
    'buvid_fp': '4740ab9e6485e28f49f6522cd558bbe9',
    'enable_feed_channel': 'DISABLE',
    'PVID': '4',
    'bp_t_offset_542348915': '1033329377200308224',
    'SESSDATA': '2b42da1e%2C1754984809%2C2b9bc%2A21CjBtWVyPrEc2E0XvFMLfKSV69rGnnm5EaD_4ZeWA6ficmP_GflzAwi0hf4DpWZFBCXESVllkTUlKOU5LZXlJRHpIb2Y5ZkhlTERLdVF0QVllNkxoaGJRRnZmdVI2d1N6X0w5MlhpTlpoOVlRdGk1cHFMaHF1dW9fVXhzekkzZWNubmhTdTFsb2ZnIIEC',
    'bili_jct': '9080149cd89a1efb675a658f7c8a25c7',
    'DedeUserID': '1209254330',
    'DedeUserID__ckMd5': '9de9846bf0c8143b',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk2OTI1MDEsImlhdCI6MTczOTQzMzI0MSwicGx0IjotMX0.bKtq3vZnCg85JK6TIp5txDqYLgmOxJ6buUd1ldx3FJE',
    'bili_ticket_expires': '1739692441',
    'browser_resolution': '1920-924',
    'sid': '5hey2t0u',
    'bp_t_offset_1209254330': '1033354051787423744',
    'b_lsid': '9F81F851_19502DB988B',
    'CURRENT_FNVAL': '4048',
}
headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/video/BV1KrNweHE64/?spm_id_from=333.788.player.switch&vd_source=242a089df30b8697da863ace8252bac8',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.467.400 QQBrowser/13.4.6232.400',
}


def get_history(oid):
    params = {
        'month': '2025-02',
        'type': '1',
        'oid': oid,
    }

    url = 'https://api.bilibili.com/x/v2/dm/history/index'
    response = requests.get(url, params=params, cookies=cookies, headers=headers)
    time_list = response.json()['data']
    logger.info(time_list)

    return time_list


def get_danmu(time_list, oid):
    url = 'https://api.bilibili.com/x/v2/dm/web/history/seg.so'
    for time in time_list:
        logger.info(f'正在采集{time}的弹幕')
        params = {
            'type': 1,  # 弹幕类型
            'oid': oid,  # cid
            'date': time  # 弹幕日期
        }
        resp = requests.get(url, params, cookies=cookies, headers=headers)
    
        DM = DmSegMobileReply()
        DM.ParseFromString(resp.content)
        data_dict = json.loads(MessageToJson(DM))
        list(map(lambda x=None: logger.info(x['content']), data_dict.get('elems', [])))
        sleep(random.randint(3,5))


if __name__ == '__main__':
    oid = '28212988412'
    time_list = get_history(oid)
    get_danmu(time_list, oid)
