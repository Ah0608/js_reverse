import time

import execjs
import requests

cookies = {
    'UOR': 'github.com,tousu.sina.com.cn,',
    'SINAGLOBAL': '45.137.183.234_1742793627.442076',
    'Apache': '45.137.183.234_1742793627.442077',
    'ULV': '1742793659495:2:2:2:45.137.183.234_1742793627.442077:1742793626741',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://tousu.sina.com.cn/company/view?couid=1003629&sid=26873',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

ts = int(time.time() * 1000)
print(ts)

params = {
    'ts': f'{ts}',
    'rs': '8IMtMFaELX4z4pXs',
    'signature': 'c835bf7ff4f442f1c08cee27b483bcdf325d5a18b355107273d4bd64de0db396',
    'type': 1,
    'page_size': 10,
    'page': 1,
    'sid': '26873',
}

with open('signature.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

rs = ctx.call('rs')
params['rs'] = rs
params['signature'] = ctx.call('getSignature', ts, rs, params['sid'], params['type'], params['page_size'],
                               params['page'])
print(params['rs'])
print(params['signature'])

response = requests.get(
    'https://tousu.sina.com.cn/api/company/service_complaints',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.json())
