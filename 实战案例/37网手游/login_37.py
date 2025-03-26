import execjs
import requests

cookies = {
    'Hm_lvt_2bff1797982a3dfe38d535d59aca3334': '1741829638',
    'HMACCOUNT': '9A1A32BD11910290',
    '37wanrefer': 'github.com',
    'PHPSESSID': '3grqieuog0pek70hbgf33n5up0',
    'Hm_lpvt_2bff1797982a3dfe38d535d59aca3334': '1741844348',
    'tg_uv': 'fG.SZ4YKgy8BAAAAxqcM',
}

headers = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://my.37.com/login.html?url=//my.37.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

user_info = {
    'login_account': '3120205442',
    'password': '123456',
}

with open('get_pwd.js','r',encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
pwd = ctx.call('encrypt_pwd',user_info['password'])
print(pwd)

params = {
    'callback': 'jQuery18303372793382444488_1741844347854',
    'action': 'login',
    'login_account': user_info['login_account'],
    'password': pwd,
    'ajax': '0',
    'remember_me': '1',
    'save_state': '1',
    'ltype': '1',
    'tj_from': '103',
    's': '1',
    'img_ver': '1.0',
    'tj_way': '1',
    '_': '1741844809493',
}

response = requests.get('https://my.37.com/api/login.php', params=params, cookies=cookies, headers=headers)
print(response.text.encode('utf-8').decode('unicode_escape'))

