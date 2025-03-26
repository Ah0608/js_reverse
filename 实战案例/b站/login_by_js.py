import json
import random
import re
import time
from time import sleep

import execjs
from curl_cffi import requests
from loguru import logger

from 日常练习.实战案例.b站.src.captcha import TextSelectCaptcha

cookies = {
    'buvid3': '15302FD7-5574-8583-FAC9-514D9EF9839F75916infoc',
    'rpdid': "|(kRk|uRJ|l0J'uYmk|~~k~)",
    'header_theme_version': 'CLOSE',
    'buvid_fp_plain': 'undefined',
    'enable_web_push': 'DISABLE',
    'LIVE_BUVID': 'AUTO8316989143482440',
    'FEED_LIVE_VERSION': 'V_WATCHLATER_PIP_WINDOW3',
    'home_feed_column': '5',
    'CURRENT_QUALITY': '80',
    'buvid4': 'C1DC1876-9A8F-841A-79B7-9DB9E3A406FC40676-023030912-c5iCHVUoavLDhv4Zp%2Br9Gg%3D%3D',
    'b_nut': '100',
    '_uuid': 'CF9101526-EFE8-4BF9-BDE1-11D104F6529CE99975infoc',
    'fingerprint': '4740ab9e6485e28f49f6522cd558bbe9',
    'buvid_fp': '4740ab9e6485e28f49f6522cd558bbe9',
    'bp_t_offset_1209254330': '1024446160766500864',
    'enable_feed_channel': 'DISABLE',
    'bmg_af_switch': '1',
    'bmg_src_def_domain': 'i0.hdslb.com',
    'CURRENT_FNVAL': '2000',
    'PVID': '4',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk2ODY4MTgsImlhdCI6MTczOTQyNzU1OCwicGx0IjotMX0.7tOYy_phlrBUyZ2F-TEHB_mDnsSS4T9_Xs9TXaKYGCY',
    'bili_ticket_expires': '1739686758',
    'b_lsid': '778FDA107_194FDF7258D',
    'sid': 'gb83fp3s',
    'bp_t_offset_542348915': '1033329377200308224',
    'browser_resolution': '1920-278',
}
headers = {
    'authority': 'www.bilibili.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.467.400 QQBrowser/13.4.6232.400',
}


class BiliBiliLogin:
    def __init__(self):
        self.session = requests.Session()

    def verify_captcha(self, gt, challenge, cc, ss, coordinate_str, pic):
        with open('doc/get_w.js', 'r', encoding='utf-8') as f:
            js_code = f.read()

        ctx = execjs.compile(js_code)
        w_value = ctx.call("get_w", gt, challenge, cc, ss, coordinate_str, pic)

        return w_value

    def get_all_info(self):
        params = {
            'source': 'main-fe',
            'web_location': '333.1228',
        }
        response = self.session.get('https://passport.bilibili.com/x/passport-login/captcha', params=params, cookies=cookies,headers=headers)
        data = response.json()

        token = data['data']['token']
        challenge = data['data']['geetest']['challenge']
        gt = data['data']['geetest']['gt']
        logger.info(f'token: {token}')
        logger.info(f'challenge: {challenge}')
        logger.info(f'gt: {gt}')

        return token, challenge, gt

    def get_captcha(self):
        token, challenge, gt = self.get_all_info()
        params1 = {
            "gt": gt,
            "callback": f'geetest_{str(int(time.time())*1000)}',
        }
        self.session.get("https://api.geetest.com/gettype.php", params=params1, cookies=cookies, headers=headers)

        params2 = {
            "gt": f"{gt}",
            "challenge": f"{challenge}",
            "lang": "zh-cn",
            "pt": "0",
            "client_type": "web",
            "w": "",
            "callback": f'geetest_{str(int(time.time())*1000)}',
        }
        self.session.get("https://api.geetest.com/get.php", headers=headers, params=params2)

        params3 = {
            "gt": gt,
            "challenge": challenge,
            "lang": "zh-cn",
            "pt": "0",
            "client_type": "web",
            "w": "",
            "callback": f'geetest_{str(int(time.time())*1000)}',
        }
        self.session.get("https://api.geetest.com/ajax.php", params=params3, headers=headers,cookies=cookies)

        params4 = {
            'is_next': 'true',
            'type': 'click',
            'gt': gt,
            'challenge': challenge,
            'lang': 'zh-cn',
            'https': 'false',
            'protocol': 'https://',
            'offline': 'false',
            'product': 'embed',
            'api_server': 'api.geetest.com',
            'isPC': 'true',
            'autoReset': 'true',
            'width': '100%',
            'callback': f'geetest_{str(int(time.time())*1000)}',
        }
        response = self.session.get('https://api.geetest.com/get.php', params=params4, headers=headers,cookies=cookies)
        data = response.text
        pattern = re.compile(r"\((.*?)\)", re.S)
        data = json.loads(pattern.findall(data)[0])
        pic = data['data']['pic']
        captcha_url = f"https://static.geetest.com{pic}?challenge={challenge}"
        c = data['data']['c']
        s = data['data']['s']
        logger.info(f'captcha_url: {captcha_url}')
        logger.info(f'c: {c}')
        logger.info(f's: {s}')

        content = self.session.get(captcha_url, headers=headers,cookies=cookies).content

        with open('image/captcha.png', 'wb') as f:
            f.write(content)

        cap = TextSelectCaptcha()
        codes = cap.run(content)
        logger.info(f'点击坐标: {codes}')
        click_coordinate = []
        for code in codes:
            x, y = (code[0] + code[2]) / 2, (code[1] + code[3]) / 2
            final_x = int(round(int(x) / 333.375 * 100 * 100, 0))
            final_y = int(round(int(y) / 333.375 * 100 * 100, 0))
            final = f"{final_x}_{final_y}"
            click_coordinate.append(final)
        coordinate_str = ",".join(click_coordinate)
        logger.info(coordinate_str)
        w_value = self.verify_captcha(gt, challenge, c, s, coordinate_str, pic)
        logger.info(f'w的值为：{w_value}')

        params5 = {
            "gt": gt,
            "challenge": challenge,
            "lang": "zh-cn",
            "pt": 0,
            "client_type": "web",
            "w": w_value,
            "callback": f'geetest_{str(int(time.time())*1000)}',
        }
        sleep(random.randint(1,2))

        url = "https://api.geetest.com/ajax.php"
        req = self.session.get(url=url, params=params5,headers=headers,cookies=cookies)
        data = req.text
        logger.info(f'验证码返回值: {data}')
        pattern = re.compile(r"\((.*)\)")
        validate = json.loads(pattern.findall(data)[0])["data"]["validate"]

        return validate, token, challenge

    def get_password(self, hash, public_key, password):
        with open("doc/get_pw.js", "r", encoding="utf-8") as f:
            code = f.read()
        run = execjs.compile(code)
        result = run.call("get_password", hash, public_key, password)
        return result

    def login(self):
        get_key_url = "https://passport.bilibili.com/x/passport-login/web/key"
        key_params = {
            "_": str(time.time() * 1000)
        }

        req = self.session.get(get_key_url, params=key_params, headers=headers,cookies=cookies)
        data = req.json()
        hash = data.get("data")["hash"]
        public_key = data.get("data")["key"]
        logger.info(f"hash: {hash}")
        logger.info(f"public_key: {public_key}")

        validate, token, challenge = self.get_captcha()

        login_url = "https://passport.bilibili.com/x/passport-login/web/login"
        user_info = {
            "username": "19946733539",
            "password": "hp200168"
        }

        login_data = {
            "source": "main_web",
            "username": user_info["username"],
            "password": self.get_password(hash, public_key, user_info["password"]),
            'go_url': 'https://www.bilibili.com/',
            "token": token,
            "validate": validate,
            "seccode": f"{validate}|jordan",
            "challenge": challenge,
            "keep":0

        }
        # 这里要加上自己的cookie，cookie中的参数有登录环境的检测
        req = self.session.post(url=login_url, data=login_data, headers=headers,cookies=cookies)
        print(req.status_code)
        print(req.text)


if __name__ == '__main__':
    bilibili = BiliBiliLogin()
    bilibili.login()