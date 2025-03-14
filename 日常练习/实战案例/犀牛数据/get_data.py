import execjs
import requests

cookies = {
    'btoken': 'B9RLV7H20SZOD76JUK6WMIO4NT0E947B',
    'hy_data_2020_id': '1956a946994120-0fe9f6f2ba6199-26011a51-2073600-1956a946995b29',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%221956a946994120-0fe9f6f2ba6199-26011a51-2073600-1956a946995b29%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%221956a946994120-0fe9f6f2ba6199-26011a51-2073600-1956a946995b29%22%7D',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1741249866',
    'HMACCOUNT': '9A1A32BD11910290',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1741311929',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

params = {"sort":1,"start":40,"limit":20}

with open('params.js','r',encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
json_data = ctx.call('get_params', params)

encrypt_text = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()['d']

decrypt_data = ctx.call('decrypt_data', encrypt_text)

print(decrypt_data)