from time import sleep

import execjs

import requests

ctx = execjs.compile(open('spa6.js', 'r', encoding='utf-8').read())
list_token = ctx.call('get_token', '/api/movie')
print('list_token', list_token)

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,es-ES;q=0.8,es;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://spa6.scrape.center/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'limit': '10',
    'offset': '0',
    'token': f'{list_token}',
}

response = requests.get('https://spa6.scrape.center/api/movie/', params=params, headers=headers)
list_json_data = response.json()
for item in list_json_data['results']:
    id = item['id']
    print('id', id)
    encrypt_id = ctx.call('idEncrype', id)
    print(encrypt_id)
    detail_url_parent = f'/api/movie/{encrypt_id}'
    print(detail_url_parent)
    detail_token = ctx.call('get_token', detail_url_parent)
    print(detail_token)
    res = requests.get('https://spa6.scrape.center/api/movie/{}?token={}'.format(encrypt_id, detail_token), )
    detail_json_data = res.json()
    movie_dict = {}
    movie_dict['m_id'] = detail_json_data['id']
    movie_dict['m_name'] = detail_json_data['name']
    movie_dict['m_alias'] = detail_json_data['alias']
    print(movie_dict)
    sleep(3)
