import json
import random
import re
import time

import execjs
from loguru import logger

from 日常练习.实战案例.b站.src.captcha import TextSelectCaptcha

import requests

from 日常练习.实战案例.b站.src.utils.utils import drow_img


# params = {
#     'challenge': 'ee6e3e54895c6501c64b9016b5dc4dc5',
# }

# content = response = requests.get(
#     'https://static.geetest.com/captcha_v3/custom_batch/v3/37/2023-05-26T18/icon/4f7f643bf6f244a38b83b9d66a55f88a.jpg',
#     params=params,
#     headers=headers,
# ).content
#
# with open('captcha.png', 'wb') as f:
#     f.write(content)
#
# cap = TextSelectCaptcha()
# codes = cap.run(content)
# logger.info(f'点击坐标: {codes}')

# cap = TextSelectCaptcha()
# result = cap.run('captcha.png')
# print(result)
# cap.yolo.infer('captcha.png')
# drow_img('captcha1.png', result)


# 点击坐标: [[138, 155, 209, 222], [209, 175, 287, 244], [224, 64, 304, 141]]


class DangleLogin:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'i',
            'referer': 'https://oauth.d.cn/',
            'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'image',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-storage-access': 'active',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        }
        self.cookies = {
            'JSESSIONID': '11641c28701057a8b1d229a8c816',
            'ut': '1742887011119',
            'BIGipServerpool_web_oauth.d.cn_auth_81': '2835458240.20736.0000',
        }
        self.gt = None
        self.challenge = None

    def verify_captcha(self, gt, challenge, cc, ss, coordinate_str, pic):
        with open('get_w.js', 'r', encoding='utf-8') as f:
            js_code = f.read()

        ctx = execjs.compile(js_code)
        w_value = ctx.call("get_w", gt, challenge, cc, ss, coordinate_str, pic)

        return w_value

    def get_all_info(self):
        params = {
            'display': 'web',
            't': '1742970135864',
        }

        data = self.session.get('https://oauth.d.cn/auth/gt/start', params=params, cookies=self.cookies,
                                headers=self.headers).json()
        self.gt = data['gt']
        self.challenge = data['challenge']

    def get_captcha(self):
        self.get_all_info()
        params1 = {
            'gt': self.gt,
            'callback': f'geetest_{int(time.time() * 1000)}',
        }

        self.session.get('https://api.geetest.com/gettype.php', params=params1, headers=self.headers)

        params2 = {
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "pt": "0",
            "client_type": "web",
            "w": "",
            "callback": f'geetest_{int(time.time() * 1000)}'
        }
        self.session.get("https://api.geetest.com/get.php", headers=self.headers, params=params2)

        params3 = {
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "pt": "0",
            "client_type": "web",
            "w": "",
            "callback": f'geetest_{int(time.time() * 1000)}'
        }
        self.session.get("https://api.geevisit.com/ajax.php", headers=self.headers, params=params3)

        params4 = {
            "is_next": "true",
            "type": "click",
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "https": "false",
            "protocol": "https://",
            "offline": "false",
            "product": "popup",
            "api_server": "api.geevisit.com",
            "isPC": "true",
            "autoReset": "true",
            "width": "100%",
            "callback": f'geetest_{int(time.time() * 1000)}'
        }
        response = self.session.get("https://api.geevisit.com/get.php", headers=self.headers, params=params4)
        data = response.text
        pattern = re.compile(r"\((.*?)\)", re.S)
        data = json.loads(pattern.findall(data)[0])
        pic = data['data']['pic']
        captcha_url = f"https://static.geetest.com{pic}?challenge={self.challenge}"
        c = data['data']['c']
        s = data['data']['s']
        logger.info(f'验证码地址：{captcha_url}')
        logger.info(f'c: {c}')
        logger.info(f's: {s}')

        content = self.session.get(captcha_url).content

        images_path = 'captcha.png'
        with open(images_path, 'wb') as f:
            f.write(content)

        cap = TextSelectCaptcha()
        result = cap.run(images_path)
        logger.info(f'验证码坐标位置：{result}')
        cap.yolo.infer(images_path)
        drow_img(images_path, result)

        click_coordinate = []
        for code in result:
            x, y = (code[0] + code[2]) / 2, (code[1] + code[3]) / 2
            final_x = int(round(int(x) / 333.375 * 100 * 100, 0))
            final_y = int(round(int(y) / 333.375 * 100 * 100, 0))
            final = f"{final_x}_{final_y}"
            click_coordinate.append(final)
        coordinate_str = ",".join(click_coordinate)
        logger.info(coordinate_str)
        w_value = self.verify_captcha(self.gt, self.challenge, c, s, coordinate_str, pic)
        logger.info(f'w的值为：{w_value}')

        params5 = {
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "pt": 0,
            "client_type": "web",
            "w": w_value,
            "callback": f'geetest_{str(int(time.time()) * 1000)}',
        }
        time.sleep(random.randint(1, 2))

        req = self.session.get("https://api.geetest.com/ajax.php", params=params5)
        data = req.text
        print(data)
        logger.info(f'验证码返回值: {data}')
        pattern = re.compile(r"\((.*)\)")
        validate = json.loads(pattern.findall(data)[0])["data"]["validate"]
        print(validate)



if __name__ == '__main__':
    dangle = DangleLogin()
    dangle.get_captcha()
