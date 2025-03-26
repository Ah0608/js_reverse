from loguru import logger

from 日常练习.实战案例.b站.src.captcha import TextSelectCaptcha

import requests

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'i',
    'referer': 'https://oauth.d.cn/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}

params = {
    'challenge': 'ee6e3e54895c6501c64b9016b5dc4dc5',
}

content = response = requests.get(
    'https://static.geetest.com/captcha_v3/custom_batch/v3/37/2023-05-26T18/icon/4f7f643bf6f244a38b83b9d66a55f88a.jpg',
    params=params,
    headers=headers,
).content

with open('captcha.png', 'wb') as f:
    f.write(content)

cap = TextSelectCaptcha()
codes = cap.run(content)
logger.info(f'点击坐标: {codes}')

# 点击坐标: [[138, 155, 209, 222], [209, 175, 287, 244], [224, 64, 304, 141]]
