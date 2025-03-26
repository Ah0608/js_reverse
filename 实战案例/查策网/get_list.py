import execjs
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.chacewang.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.chacewang.com/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}

params = {
    'page': '3',
    'size': '20',
    'industry': '',
    'area': 'RegisterArea_HNDQ_Guangdong_SZ',
    'dept': '',
    'partition': '',
    'pe_name': '',
    'currentArea': 'RegisterArea_HNDQ_Guangdong_SZ',
    'query_date': '0',
    'full_search': '0',
    'sort_type': '0',
}

encrypt_data = requests.get('https://web.chace-ai.com/api/ccw/project/evaluation/getList/', params=params, headers=headers).json()['data']

with open('decrypt_data.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
decrypt_data = ctx.call('u', encrypt_data)
print(decrypt_data)

