import json
import re

import requests
import execjs

with open('decrypt.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

cookies = {
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221954a18f6e760d-03e462e5d3c605-26011a51-2073600-1954a18f6e8eac%22%2C%22%24device_id%22%3A%221954a18f6e760d-03e462e5d3c605-26011a51-2073600-1954a18f6e8eac%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    'Hm_lvt_1684191ccae0314c6254306a8333d090': '1740704905',
    'HMACCOUNT': '9A1A32BD11910290',
    'Hm_lvt_713123c60a0e86982326bae1a51083e1': '1740704905',
    'Hm_lpvt_1684191ccae0314c6254306a8333d090': '1740705244',
    'Hm_lpvt_713123c60a0e86982326bae1a51083e1': '1740705244',
    'SERVERID': 'd36083915ff24d6bb8cb3b8490c52181|1740706086|1740704905',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://36kr.com/p/3182854979327360', cookies=cookies, headers=headers)
json_data = json.loads(re.findall('window.initialState=(.*?)</script>', response.text)[0])
encrypt_text = json_data['state']

decrypt_text = ctx.call('decrypt', encrypt_text)
print(decrypt_text)

