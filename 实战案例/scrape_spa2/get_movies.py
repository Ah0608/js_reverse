import execjs
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://spa2.scrape.center/page/1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'limit': '10',
    'offset': '0',
    'token': 'MzU3MzljYjlkNjYxZDExODdmYmFmYjI4ZThiZDQ2NzhjMmRiNTE4YiwxNzQyMzUxNjE2',
}

with open('get_token.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
token = ctx.call('get_token', ["/api/movie", int(params['offset'])])
print(token)
params['token'] = token

response = requests.get('https://spa2.scrape.center/api/movie/', params=params, headers=headers)
print(response.json())
