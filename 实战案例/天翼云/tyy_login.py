import execjs
import requests

cookies = {
    'Hm_lvt_4b4ce93f1c92033213556e55cb65769f': '1740988399',
    'HMACCOUNT': '9A1A32BD11910290',
    'Hm_lpvt_4b4ce93f1c92033213556e55cb65769f': '1740988448',
    'pvid': '7',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Csm': '726d27edfe809af910423fcc27ba505e2723617d9e2a1ad3af8147d6e84a3298',
    'Cst': '1740991405286',
    'Origin': 'https://m.ctyun.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-riskdevicesign': '3b664f7b1bdd040317db88d0a4041f63',
}

with open('login.js', 'r', encoding='utf-8') as f:
    js = f.read()

ctx = execjs.compile(js)

pwd = ctx.call('get_pwd', '123456@163.com', 'dasdadasda')
print(pwd)

params_data = ctx.call('get_params')
print(params_data)

data = {
    'userName': '123456@163.com',
    'password': pwd,
}

params = {
    'referrer': 'wap',
    'mainVersion': '300031500',
    'comParam_curTime': params_data['comParam_curTime'],
    'comParam_seqCode': params_data['comParam_seqCode'],
    'comParam_signature': params_data['comParam_signature'],
    'isCheck': 'true',
    'locale': 'zh-cn',
}

response = requests.post('https://m.ctyun.cn/account/login', params=params, cookies=cookies, headers=headers, data=data)
print(response.text)

