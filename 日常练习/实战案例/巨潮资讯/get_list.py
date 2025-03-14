import requests

cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1741070929',
    'HMACCOUNT': '9A1A32BD11910290',
    'MALLSSID': '716B695074776F356559767978676E74582B5852304150335667495174484B77496778336773587574784150643071614C7559344D49626F42417359594B7869',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1741071306',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-EncKey': '1JGvHm0HnUDsdlFOP/2Ubg==',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1128', cookies=cookies, headers=headers)
print(response.text)

