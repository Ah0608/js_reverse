import json
import time

import execjs
import requests


def get_car_peizhi(cid,cityId,serialId):
    ts = int(time.time() * 1000)
    par = json.dumps({"cityId":f"{cityId}","serialId":f"{serialId}"})
    print(par)

    with open('get_headers.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    sign = ctx.call('get_sign', cid,par,ts)
    print(sign)

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cid': cid,
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://car.yiche.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://car.yiche.com/yunqueq1/peizhi/',
        'reqid': 'e90b492d250443e340480f1c2ca8d30f',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'x-city-id': cityId,
        'x-ip-address': '125.80.199.34',
        'x-platform': 'pc',
        'x-sign': sign,
        'x-timestamp': f'{ts}',
        'x-user-guid': '61e87bed7ab784c82210583afdc03875',
    }

    params = {
        'cid': cid,
        'param': par,
    }

    response = requests.get(
        'https://mhapi.yiche.com/hcar/h_car/api/v1/param/get_param_details',
        params=params,
        headers=headers,
    )

    print(response.json())


if __name__ == '__main__':
    cid = '508' # 车辆id
    cityId = '201' # 城市id
    serialId = '5485' # 车系id
    get_car_peizhi(cid,cityId,serialId)