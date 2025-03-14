import json
import time
from curl_cffi import requests
import execjs


cookies = {
    'OUTFOX_SEARCH_USER_ID_NCOO': '157146546.7759259',
    'OUTFOX_SEARCH_USER_ID': '-729964114@14.108.216.157',
    '_ga': 'GA1.2.1061115304.1694412776',
    'P_INFO': '18723561307|1735183407|1|youdao_zhiyun2018|00&99|null&null&null#chq&null#10#0#0|&0||18723561307',
    'DICT_DOCTRANS_SESSION_ID': 'MTgyNTMxYWMtY2JjYS00Nzk5LWJmNWEtMTRmNGNjYzRkZDBl',
    '_uetsid': 'f9b79d00da0011ef8f311b46e3e2446a',
    '_uetvid': '62413d204fce11ef8b68af129f8f06c2',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.467.400 QQBrowser/13.4.6232.400',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

with open('run.js', 'r', encoding='utf-8') as f:
    js = f.read()
ctx = execjs.compile(js)


def get_secret_key():
    ts = int(time.time() * 1000)
    sign = ctx.call('sign', ts ,'asdjnjfenknafdfsdfsd')
    params = {
        "keyid": "webfanyi-key-getter",
        "sign": sign,
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": ts,
        "keyfrom": "fanyi.web",
        "mid": "1",
        "screen": "1",
        "model": "1",
        "network": "wifi",
        "abtest": "0",
        "yduuid": "abcdefg"
    }
    response = requests.get('https://dict.youdao.com/webtranslate/key', cookies=cookies, headers=headers, params=params)
    data = response.json()
    return data['data']['secretKey']


def translate(str):
    secretKey = get_secret_key()
    ts = int(time.time() * 1000)
    sign = ctx.call('sign', ts, secretKey)
    data = {
        'i': f'{str}',
        'from': 'auto',
        'to': '',
        'useTerm': 'false',
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': f'{sign}',
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': f'{ts}',
        'keyfrom': 'fanyi.web',
        'mid': '1',
        'screen': '1',
        'model': '1',
        'network': 'wifi',
        'abtest': '0',
        'yduuid': 'abcdefg',
    }

    response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)
    encodeStr = response.text
    decodeData = json.loads(ctx.call('getresult', encodeStr))
    print(decodeData)
    res = decodeData["translateResult"][0][0]["tgt"]
    print('{}\n翻译结果:{}'.format(str, res))


if __name__ == '__main__':
    while True:
        str = input('请输入要翻译的内容:')
        translate(str)
