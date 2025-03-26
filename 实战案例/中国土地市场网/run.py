import execjs
from curl_cffi import requests

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
url = 'https://api.landchina.com/tGdxm/result/list'
url_param = url.split('/')[-1]
with open('get_hash.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
ctx = execjs.compile(jscode)
hash = ctx.call('getHash',ua,url_param)
print(hash)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Hash': hash,
    'Origin': 'https://www.landchina.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.landchina.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': ua,
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'pageNum': 1,
    'pageSize': 10,
    'startDate': '',
    'endDate': '',
}

response = requests.post(url, headers=headers, json=json_data, impersonate='chrome110')
print(response.json())
