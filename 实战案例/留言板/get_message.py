import json

import execjs
import requests

cookies = {
    '__jsluid_h': 'd90107c52b67f056326c21b1fbaca6ea',
    'language': 'zh-CN',
    'deviceId': 'ece1a3bd-3464-4f3d-8fdd-33b6527f6a4c',
    'Hm_lvt_40ee6cb2aa47857d8ece9594220140f1': '1742373165',
    'HMACCOUNT': '9A1A32BD11910290',
    '__jsluid_s': 'd321eb02fe0170d2464d6d308ef55493',
    'wdcid': '747593353e805fdb',
    'Hm_lpvt_40ee6cb2aa47857d8ece9594220140f1': '1742387125',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://liuyan.people.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://liuyan.people.com.cn/messageSearch',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'token': '',
}

json_data = {
    'appCode': 'PC42ce3bfa4980a9',
    'token': '',
    'signature': '15645586216c596864732b57a474b715',
    'param': '{"position":0,"keywords":"","fid":null,"domainId":null,"typeId":null,"timeRange":null,"ansChecked":false,"stTime":null,"sortType":"0","page":1,"rows":10}',
}
url = 'https://liuyan.people.com.cn/v2/threads/search?sortType=0'

with open('get_signature.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

json_data['signature'] = ctx.call('get_signature', url.split('.cn')[-1], json.loads(json_data['param']), json_data['appCode'])
print(json_data)
response = requests.post(
    url,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.json())
