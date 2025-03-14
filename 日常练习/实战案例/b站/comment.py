import requests
from loguru import logger

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
    'fingerprint': '4740ab9e6485e28f49f6522cd558bbe9',
    'buvid_fp': '4740ab9e6485e28f49f6522cd558bbe9',
    'enable_feed_channel': 'DISABLE',
    'bp_t_offset_542348915': '1033329377200308224',
    'DedeUserID': '1209254330',
    'DedeUserID__ckMd5': '9de9846bf0c8143b',
    'browser_resolution': '1920-924',
    'bp_t_offset_1209254330': '1033354051787423744',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk5NDk5MDIsImlhdCI6MTczOTY5MDY0MiwicGx0IjotMX0.CyzX1nLQLu4sESvGy74n4WuJgeiJCtWGlO83R59KTLE',
    'bili_ticket_expires': '1739949842',
    'PVID': '5',
    'b_lsid': 'DDCDB8EB_19511B78498',
    'SESSDATA': '0b527d18%2C1755310996%2C3b05d%2A21CjCcE4fgtq7Z8MzJa7tcnNKvFtVY3uxPciNt63IG7lUvquFcAwcGZGnQfj9TbP6zC9YSVmJ3QThEM0k0UG5Gc1NCMDZiZHBESXZISkI2WlROa1hoX0w2aGVJWGRXTDhqbGlQcUd1SGw4YUtGbm0zTWdWLVBySWk4VW9PTXQ1UkVzZWtqTjU3empBIIEC',
    'bili_jct': '759e583a8fadd89451977f3e8ea3918b',
    'sid': '7z6csca0',
    'CURRENT_FNVAL': '4048',
}
headers = {
    'authority': 'api.bilibili.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/video/BV19uNTemEDM/?spm_id_from=333.1007.tianma.2-1-4.click&vd_source=242a089df30b8697da863ace8252bac8',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.467.400 QQBrowser/13.4.6232.400',
}


def get_comment_count(oid):
    params = {
        'oid': oid,
        'type': '1',
    }
    response = requests.get(
        'https://api.bilibili.com/x/v2/reply/count',
        cookies=cookies,
        headers=headers,
        params=params,
    )
    logger.info(response.json())


def get_comment_tree(oid):
    '''
    oid: 目标评论区 id
    type: 评论区类型代码
    root: 根回复 rpid
    dialog: 对话树根 rpid
    size: 每页最大项数
    '''
    params = {
        'oid': oid,
        'type': '1',
        'root': '254741574064',
        'dialog': '254892755648',
        'size': '5',
    }
    response = requests.get(
        'https://api.bilibili.com/x/v2/reply/dialog/cursor',
        cookies=cookies,
        headers=headers,
        params=params,
    )
    comment_tree_data = response.json()
    logger.info(comment_tree_data)
    logger.info(f'该对话共有{comment_tree_data["data"]["cursor"]["size"]}层')
    for comment in comment_tree_data["data"]["replies"]:
        logger.info(f'评论人：{comment["member"]["uname"]}')
        logger.info(f'评论内容：{comment["content"]["message"]}'.replace("\n",""))
        logger.info(f'点赞数：{comment["like"]}')
        logger.info(f'回复数：{comment["rcount"]}')
        logger.info('*' * 20)


def get_all_comment_by_page(oid):
    '''
    oid: 目标评论区 id
    type: 评论区类型代码
    sort: 排序方式 (默认为0, 0：按时间、1：按点赞数、2：按回复数)
    nohot: 是否不显示热评 (默认为0, 1：不显示、0：显示)
    ps: 每页项数 (默认为20, 定义域：1-20)
    pn: 页码 (默认为1)
    '''
    params = {
        'oid': oid,
        'type': '1',
        'sort': '1',
        'nohot': '1',
        'ps': '20',
        'pn': '1',
    }
    response = requests.get(
        'https://api.bilibili.com/x/v2/reply',
        cookies=cookies,
        headers=headers,
        params=params,
    )
    comment_data = response.json()
    logger.info(f'当前视频[{params["oid"]}]评论共{comment_data["data"]["page"]["count"]}条，每页显示{params["ps"]}条，评论目前是第{params["pn"]}页.')
    logger.info('-' * 20)
    for comment in comment_data["data"]["replies"]:
        logger.info(f'评论人：{comment["member"]["uname"]}')
        logger.info(f'评论内容：{comment["content"]["message"]}'.replace("\n",""))
        logger.info(f'点赞数：{comment["like"]}')
        logger.info(f'回复数：{comment["rcount"]}')
        logger.info('*' * 20)
        for reply in comment["replies"]:
            logger.info(f'回复人：{reply["member"]["uname"]}')
            logger.info(f'回复内容：{reply["content"]["message"]}'.replace("\n",""))
            logger.info(f'点赞数：{reply["like"]}')
            logger.info(f'回复数：{reply["rcount"]}')
            logger.info('#' * 20)


def get_one_comment_reply(oid):
    '''
    oid: 目标评论区 id
    type: 评论区类型代码
    root: 根回复 rpid
    ps: 每页项数 (默认为20, 定义域：1-20)
    pn: 页码 (默认为1)
    '''
    params = {
        'oid': oid,
        'type': '1',
        'root': '254741574064',
        'ps': '20',
        'pn': '1',
    }
    response = requests.get(
        'https://api.bilibili.com/x/v2/reply/reply',
        cookies=cookies,
        headers=headers,
        params=params,
    )
    reply_data = response.json()
    logger.info(f'当前评论[{params["root"]}]-（{reply_data["data"]["root"]["content"]["message"]}）-回复共{reply_data["data"]["page"]["count"]}条，每页显示{params["ps"]}条，评论目前是第{params["pn"]}页.'.replace("\n",""))
    for reply in reply_data["data"]["replies"]:
        logger.info(f'回复人：{reply["member"]["uname"]}')
        logger.info(f'回复内容：{reply["content"]["message"]}'.replace("\n",""))
        logger.info(f'点赞数：{reply["like"]}')
        logger.info(f'回复数：{reply["rcount"]}')
        logger.info('#' * 20)


if __name__ == '__main__':
    oid = '113963819863689'
    # get_all_comment_by_page(oid)
    # get_comment_count(oid)
    # get_one_comment_reply(oid)
    get_comment_tree(oid)
