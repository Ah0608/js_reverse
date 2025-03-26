import json
import pprint
import random
import re
import time

import ddddocr
import execjs
import requests
from loguru import logger

cookies = {
    'global_cookie': 'grtvgo8ian51vurrfi9eeqr8q12m7oi5205',
    'g_sourcepage': 'txz_dl%5Egg_pc',
    '__utmc': '147393320',
    'token': 'f5716a8d042e440b99803cd15fbb2ef5',
    'unique_cookie': 'U_grtvgo8ian51vurrfi9eeqr8q12m7oi5205*3',
    '__utma': '147393320.1727401436.1740730746.1740730746.1740972159.2',
    '__utmz': '147393320.1740972159.2.2.utmcsr=github.com|utmccn=(referral)|utmcmd=referral|utmcct=/liyf-code/reverse_practice',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://passport.fang.com',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.fang.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class FangLogin:
    def __init__(self):
        self.session = requests.Session()
        self.gt = None
        self.challenge = None
        self.distance = None
        self.captcha_ctx = None
        self.pwd_ctx = None
        self.validate = None

    def get_js_ctx(self):
        with open('captcha.js', 'r', encoding='utf-8') as f:
            captcha_js_code = f.read()

        with open('pwd.js', 'r', encoding='utf-8') as f:
            pwd_js_code = f.read()

        self.captcha_ctx = execjs.compile(captcha_js_code)
        self.pwd_ctx = execjs.compile(pwd_js_code)

    def get_slide_track(self, distance):
        track = []
        start = {
            "x": 0,
            "y": 300,
            "t": int(time.time() * 1000),
            "e": "mousedown"
        }
        track.append(start)

        x, y, t = start['x'], start['y'], start['t']
        while distance >= x:
            x += random.choices([0, 1, 2], weights=[0.3, 0.4, 0.3], k=1)[0]
            y += random.choices([0, 1, 2], weights=[0.3, 0.4, 0.3], k=1)[0]
            t += random.randint(0, 20)
            track.append({
                "x": x,
                "y": y,
                "t": t,
                "e": "mousemove"
            })

        end = {
            "x": x,
            "y": y,
            "t": t + 30,
            "e": "mouseup"
        }
        track.append(end)

        return track

    def get_all_info(self):
        info_data = self.session.post('https://passport.fang.com/getslidecodeinit.api', cookies=cookies, headers=headers).json()
        self.gt = info_data['gt']
        self.challenge = info_data['challenge']
        logger.info(f'gt: {self.gt}')
        logger.info(f'challenge: {self.challenge}')

    def get_captcha(self):
        self.get_all_info()

        params = {
            "c": "index",
            "a": "getType",
            "gt": self.gt,
            "challenge": self.challenge,
            "time": f"{str(int(time.time())*1000)}",
            "callback": f"fangcheck_{str(int(time.time())*1000)}",
            "_200226": ""
        }
        self.session.get("https://recaptcha.fang.com/", headers=headers, params=params) # 后台校验否则验证码通不过

        params = {
            "c": "index",
            "a": "jigsaw",
            "gt": self.gt,
            "challenge": self.challenge,
            "callback": f"fangcheck_{str(int(time.time())*1000)}",
            "_200226": ""
        }
        data = self.session.get("https://recaptcha.fang.com/", params=params, cookies=cookies, headers=headers).text

        pattern = re.compile(r"\((.*?)\)", re.S)
        data = json.loads(pattern.findall(data)[0])

        bg_url = f'https://static.soufunimg.com/common_m/m_recaptcha/jigsawimg/{data["url"]}'
        sb_url = f'https://static.soufunimg.com/common_m/m_recaptcha/jigsawimg/{data["surl"]}'
        bg_data = self.session.get(bg_url, cookies=cookies, headers=headers).content
        sb_data = self.session.get(sb_url, cookies=cookies, headers=headers).content
        with open('bg.jpg', 'wb') as f:
            f.write(bg_data)

        with open('sb.png', 'wb') as f:
            f.write(sb_data)

        return bg_data, sb_data

    def get_distance(self):
        bg_data, sb_data = self.get_captcha()
        slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

        res = slide.slide_match(sb_data, bg_data, simple_target=True)['target'][0]
        self.distance = int(int(res) * (300/320))
        logger.info(self.distance)

    def verify_captcha(self):
        self.get_distance()
        time.sleep(3)
        track = self.get_slide_track(self.distance)
        logger.info(track)
        i = self.captcha_ctx.call('get_i')
        t = self.captcha_ctx.call('get_t',track)
        params = {
            "c": "index",
            "a": "codeDrag",
            "start": track[0]['t'],
            "end": track[len(track)-1]['t'],
            "i": i,
            "t": t,
            "gt": self.gt,
            "challenge": self.challenge,
            "callback": f"fangcheck_{str(int(time.time())*1000)}",
            "_200226": ""
        }
        pprint.pprint(params)
        res_data = self.session.get("https://recaptcha.fang.com/", params=params, cookies=cookies, headers=headers).text

        pattern = re.compile(r"\((.*?)\)", re.S)
        data = json.loads(pattern.findall(res_data)[0])
        self.validate = data['validate']

    def login(self):
        self.get_js_ctx()
        self.verify_captcha()
        pwd = self.pwd_ctx.call('get_pwd',user_info['pwd'])
        data = {
            'uid': user_info['username'],
            'pwd': pwd,
            'Service': 'soufun-passport-web',
            'AutoLogin': '1',
            'Operatetype': '0',
            'Gt': self.gt,
            'Challenge': self.challenge,
            'Validate': self.validate,
        }

        response = self.session.post('https://passport.fang.com/loginwithpwdStrong.api', cookies=cookies, headers=headers,data=data)
        logger.info(response.text)


if __name__ == '__main__':
    user_info = {'username':'18723561307','pwd':'adadadad'}
    fang = FangLogin()
    fang.login()
