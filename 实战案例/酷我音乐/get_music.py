import execjs
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.kuwo.cn/search/list?key=%E5%85%8D%E8%B4%B9%E6%AD%8C%E6%9B%B2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Secret': '6d03bdd269123b41b556f0a32dd3f64c7c89a08f7c94f53f60e210cbeed23dca0472b48f',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1742352739; _ga=GA1.2.103907758.1742355061; _gid=GA1.2.770502556.1742355061; _ga_ETPBRPM9ML=GS1.2.1742364987.2.1.1742366834.60.0.0; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1742367614; Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324=NS6px5SjksP2fiGatFQXKni8ibkRhTXF; _gat=1',
}
with open('get_encrypt.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
Secret = ctx.call('get_secret', headers['Cookie'])
print(Secret)
headers['Secret'] = Secret

reqId = ctx.call('get_reqid')
print(reqId)

params = {
    'mid': '3965811',
    'type': 'music',
    'httpsStatus': '1',
    'reqId': 'ce8962b1-048f-11f0-af1a-9d6a93144a0a',
    'plat': 'web_www',
    'from': '',
}
params['reqId'] = reqId

res_data = requests.get('https://www.kuwo.cn/api/v1/www/music/playUrl', params=params, headers=headers).json()
music_url = res_data['data']['url']
print(music_url)

with open('music.mp3', 'wb') as f:
    f.write(requests.get(music_url,headers=headers).content)
print('下载完成')
