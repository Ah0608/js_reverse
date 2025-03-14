# _*_ coding : utf-8 _*_
# @Time : 2024/8/13 0013 19:51
# @Author :HuangPeng
# @File : run_translate
# @Project : js_nixiang
import time

import execjs
from curl_cffi import requests


def translate(word):
    with open('translate.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    token = ctx.call('get_token')
    print(f'token：{token}')
    sign = ctx.call('get_sign', word)
    print(f'sign：{sign}')
    ts = int(time.time())
    print(f'ts：{ts}')
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Acs-Token": "1723532407784_1723549755061_Hj4yuTyH7voVKXHBJcnqxfhdIS4jPz00YEmqTY9DoHLjLoxu3gdrDXcM/Ja8cwuaHl5E7T4d0PMdPkS8N+SP7N/KQ87VL12gPM+bcPW2L/Td8ulA8rg3P2SgeB/l9JfqK06qBSK3yo8xHgvFSLwY+stV7ylWV58tCyc2EAVWqSwjHv8tuNeGhLhRwHI+tavJPskED3HOr1WoIntfMqIbbz5qDXGowginZbXl4josisUQtUQxr09dMUAZ4yRZWxp6TMblNzCFoPch5IYQjQLSCOvDdJL5SWmOxfVbJHviV7AoXmin/P/YW31SzXxJgEaTMpfQh5B76d3Aizk8OZU+BEF3nDGgbmn7f5pkDX7Pav75QKvwYSTiMy38riJxEYKKBxk3fGLRSl/Bd81SnxWCxcXwGND2Q7cC8xhZIaJvkDnosE2xfxiDSRhmrAed3mpH",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://fanyi.baidu.com",
        "Referer": "https://fanyi.baidu.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "BAIDUID_BFESS": "20EF4A70D65B6B219557A7515FF5F907:FG=1",
        "BIDUPSID": "20EF4A70D65B6B219557A7515FF5F907",
        "PSTM": "1718506780",
        "H_PS_PSSID": "60325_60340",
        "ZFY": "B2yqO8HO3TzJT5a8EKjlNth09b3MVhpPz:ARvzUDzuQo:C",
        "smallFlowVersion": "old",
        "RT": "\"z=1&dm=baidu.com&si=88ef1127-0cfe-49c8-875f-7dc659cc6e96&ss=lzscnypy&sl=2&tt=3fh&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=asd&ul=hhl&hd=hnz\"",
        "REALTIME_TRANS_SWITCH": "1",
        "FANYI_WORD_SWITCH": "1",
        "HISTORY_SWITCH": "1",
        "SOUND_SPD_SWITCH": "1",
        "SOUND_PREFER_SWITCH": "1",
        "Hm_lvt_64ecd82404c51e03dc91cb9e8c025574": "1723549178",
        "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574": "1723549178",
        "ab_sr": "1.0.1_NjFmOTg0ODZiZTkwYzg0NTNlZDYzY2YwMGVkYjViNWYxOTI2ZDk1NmRmYjY1MTNiZDFjMWUwNWEzYWVlMmEyMTc1MDA0ZjU4MDc5NTEwNGQxNTBiNGU2YmNhYTA4N2RjNjc4YjMzMzlmN2EzMWNkOGNiN2MxYzRjOWU3YTgxZjk5ZWQyY2YyY2NiOGM1NDFhZDlhZGY4N2FjZWIyM2FlNw=="
    }
    url = "https://fanyi.baidu.com/v2transapi"
    params = {
        "from": "en",
        "to": "zh"
    }
    data = {
        "from": "en",
        "to": "zh",
        "query": word,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": sign,
        "token": token,
        "domain": "common",
        "ts": ts
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

    result = response.json()["trans_result"]["data"][0]["dst"]
    print("翻译结果：",result)


if __name__ == '__main__':
    translate('Cyber security guru Tingtao Hu')