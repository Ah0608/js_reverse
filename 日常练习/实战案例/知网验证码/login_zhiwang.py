import base64
import json

import ddddocr
import requests
import execjs

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://bar.cnki.net/bar/dist/index.html?platform=NZKPT&returnUrl=https://kns.cnki.net/kcms2/article/abstract?v=3uoqIhG8C44YLTlOAiTRKibYlV5Vjs7iy_Rpms2pqwbFRRUtoUImHTkGfiqQI9USUw47-t3lA6gScCwExAny5HmZH_-0oRbZ&uniplatform=NZKPT',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="109", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def save_base64_image(base64_data, output_path):
    if base64_data.startswith("data:image"):
        base64_data = base64_data.split(",")[1]

    image_data = base64.b64decode(base64_data)

    with open(output_path, "wb") as file:
        file.write(image_data)

    print(f"图片已成功保存为 {output_path}")


def get_distance(bg,target):
    slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

    with open(target, 'rb') as f:
        target_bytes = f.read()

    with open(bg, 'rb') as f:
        background_bytes = f.read()

    res = slide.slide_match(target_bytes, background_bytes, simple_target=True)['target'][0]

    print(res)
    return res


def get_captcha():

    params = {
        'captchaType': 'blockPuzzle',
    }

    response = requests.get('https://bar.cnki.net/captcha/captcha/get', params=params,headers=headers)
    captcha_json = response.json()
    secretKey = captcha_json['repData']['secretKey']
    token = captcha_json['repData']['token']
    bg_base64 = captcha_json['repData']['originalImageBase64']
    target_base64 = captcha_json['repData']['jigsawImageBase64']
    save_base64_image(bg_base64, 'bg.png')
    save_base64_image(target_base64, 'target.png')
    distance = get_distance('bg.png', r'target.png')
    print("secretKey:", secretKey, "token:", token)

    return secretKey,token,distance


def get_point_json(distance,key):
    with open('captcha.js', 'r', encoding='utf-8') as f:
        js = f.read()
    ctx = execjs.compile(js)
    param = {"x":distance,"y":5}
    param = json.dumps(param).replace(' ','')
    print('param:',param)
    pointJson = ctx.call('u',param,key)
    print(pointJson)
    return pointJson


def verify_captcha(pointJson,token):

    json_data = {
        'captchaType': 'blockPuzzle',
        'pointJson': pointJson,
        'token': token,
    }

    response = requests.post('https://bar.cnki.net/captcha/captcha/check',  headers=headers,json=json_data)
    print(response.json())


def main():
    secretKey,token,distance = get_captcha()
    pointJson = get_point_json(distance,secretKey)
    verify_captcha(pointJson,token)


if __name__ == '__main__':
    main()
