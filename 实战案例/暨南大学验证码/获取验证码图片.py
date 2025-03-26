import json
import re

import requests
import execjs

with open('滑块验证码.js', 'r', encoding='utf-8') as f:
    js = f.read()
ctx = execjs.compile(js)
jsonp = ctx.call('jsonp')
print(jsonp)

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://icas.jnu.edu.cn/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="109", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'referer': 'https://icas.jnu.edu.cn/cas/login',
    'zoneId': '',
    'id': '5a63b6131a824620af00177ddfa3d19e',
    'ipv6': 'false',
    'runEnv': '10',
    'iv': '4',
    'loadVersion': '2.5.0',
    'callback': jsonp,
}

response = requests.get('https://c.dun.163.com/api/v2/getconf', params=params, headers=headers)
data = json.loads(re.search('\((.*?)\)',response.text).group(1))
print(data)
dt = data['data']['dt']
print(dt)

'ZgK53u/adGtY8OwEV2/6mAXxa9MGxLZeZCHuVdlO/r4L+e2yM7H/BcnkbiGgzSrxtXezqxxVyrQqZDK8PPV6bslDSBQP9gQKe5w16M93PJs='


