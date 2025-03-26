import execjs
import requests

session = requests.Session()
cookies = {
    'sajssdk_2015_cross_new_user': '1',
    'acw_tc': '0b6e704a17412375704726759edaecdf57b139c40fdee3efc0929ad8c32c43',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221956990928e75b-058086d905447a4-26011a51-2073600-1956990928ff51%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgithub.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk1Njk5MDkyOGU3NWItMDU4MDg2ZDkwNTQ0N2E0LTI2MDExYTUxLTIwNzM2MDAtMTk1Njk5MDkyOGZmNTEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221956990928e75b-058086d905447a4-26011a51-2073600-1956990928ff51%22%7D',
    'Hm_lvt_e7351028cde0d0ccb9ccdbe5fe531683': '1741237597',
    'Hm_lpvt_e7351028cde0d0ccb9ccdbe5fe531683': '1741237597',
    'HMACCOUNT': '9A1A32BD11910290',
}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://fenbi.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fenbi.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

# 必须请求该接口不然登录报错
params = {
    'project': 'production',
}
data = {
    'data': 'eyJpZGVudGl0aWVzIjp7IiRpZGVudGl0eV9jb29raWVfaWQiOiIxOTU2OTkwOTI4ZTc1Yi0wNTgwODZkOTA1NDQ3YTQtMjYwMTFhNTEtMjA3MzYwMC0xOTU2OTkwOTI4ZmY1MSJ9LCJkaXN0aW5jdF9pZCI6IjE5NTY5OTA5MjhlNzViLTA1ODA4NmQ5MDU0NDdhNC0yNjAxMWE1MS0yMDczNjAwLTE5NTY5OTA5MjhmZjUxIiwibGliIjp7IiRsaWIiOiJqcyIsIiRsaWJfbWV0aG9kIjoiY29kZSIsIiRsaWJfdmVyc2lvbiI6IjEuMjYuNiJ9LCJwcm9wZXJ0aWVzIjp7IiR0aW1lem9uZV9vZmZzZXQiOi00ODAsIiRzY3JlZW5faGVpZ2h0IjoxMDgwLCIkc2NyZWVuX3dpZHRoIjoxOTIwLCIkdmlld3BvcnRfaGVpZ2h0Ijo1MjAsIiR2aWV3cG9ydF93aWR0aCI6MTkyMCwiJGxpYiI6ImpzIiwiJGxpYl92ZXJzaW9uIjoiMS4yNi42IiwiJGxhdGVzdF90cmFmZmljX3NvdXJjZV90eXBlIjoi5byV6I2Q5rWB6YePIiwiJGxhdGVzdF9zZWFyY2hfa2V5d29yZCI6IuacquWPluWIsOWAvCIsIiRsYXRlc3RfcmVmZXJyZXIiOiJodHRwczovL2dpdGh1Yi5jb20vIiwiYXBwIjoi57KJ56yU572RIiwicGxhdGZvcm1fdHlwZSI6IldlYiIsImlzX2xvZ2luIjpmYWxzZSwiY3VycmVudF9wYWdlIjoi55m75b2VIiwiYnV0dG9uX25hbWUiOiLnmbvlvZUiLCIkaXNfZmlyc3RfZGF5Ijp0cnVlLCIkdXJsIjoiaHR0cHM6Ly9mZW5iaS5jb20vcGFnZS9ob21lIiwiJHRpdGxlIjoi5YWs5Yqh5ZGY44CB5LqL5Lia5Y2V5L2N44CB5pWZ5biI44CB6LSi5Lya562J6ICD6K+V5Z+56K6tLeeyieeslOaVmeiCsiJ9LCJhbm9ueW1vdXNfaWQiOiIxOTU2OTkwOTI4ZTc1Yi0wNTgwODZkOTA1NDQ3YTQtMjYwMTFhNTEtMjA3MzYwMC0xOTU2OTkwOTI4ZmY1MSIsInR5cGUiOiJ0cmFjayIsImV2ZW50IjoiY2xpY2tfcmVnaXN0ZXJfYnV0dG9uIiwidGltZSI6MTc0MTI0MTA3NTYyNCwiX3RyYWNrX2lkIjo4NTQyNDU2MjUsIl9mbHVzaF90aW1lIjoxNzQxMjQxMDc1NjI1fQ==',
    'ext': 'crc=-516154999',
}
response = session.post('https://data-api.fenbi.com/sa', params=params, cookies=cookies, headers=headers, data=data)

# 发送登录请求
user_info = {
    'phone': '18723561304',
    'password': '123456',
}

with open('login.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
encrypt_pwd = ctx.call('get_pwd', user_info['password'])
print(encrypt_pwd)

params = {
    'app': 'web',
    'av': '100',
    'hav': '100',
    'kav': '100',
    'client_context_id': '3ff2a5678468e40303865a61e075003f',
}
data = {
    'password': encrypt_pwd,
    'persistent': 'true',
    'app': 'web',
    'phone': user_info['phone'],
}

login_info = session.post('https://login.fenbi.com/api/users/loginV2', params=params, cookies=cookies, headers=headers, data=data).json()
print(login_info)

