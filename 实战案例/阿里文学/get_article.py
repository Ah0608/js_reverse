import json
import random
from time import sleep

import execjs
import requests
from parsel import Selector

with open('decodecont.js','r',encoding='utf-8') as f:
    js_str = f.read()
ctx = execjs.compile(js_str)

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.aliwx.com.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.aliwx.com.cn/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}

_params = {
    'bid': '6813923',
    'cid': '674178',
}

response = requests.get('https://www.aliwx.com.cn/reader', params=_params, headers=headers)
html = response.text
sel = Selector(html)
str_data = sel.css('i.js-dataChapters::text').get(default='')
item = json.loads(str_data)  # 字符串转字典
data_list = item['chapterList']
info = {
    volumedata['volumeName']: {
        # 判断是否为收费章节的条件为 isFreeRead 字段
        chapterdata['chapterName']: chapterdata['contUrlSuffix'] if chapterdata['isFreeRead'] else None
        for chapterdata in volumedata['volumeList']
    }
    for volumedata in data_list
}

for volume,_item in info.items():
    for article_name, contUrlSuffix in _item.items():
        if contUrlSuffix:
            print(volume,article_name,contUrlSuffix)
            # 获取文章内容
            response = requests.get(f'https://c13.shuqireader.com/pcapi/chapter/contentfree/{contUrlSuffix}', headers=headers)
            ChapterContent = response.json()['ChapterContent']
            article_content = ctx.call('_decodeCont', ChapterContent)
            print(article_content)
            sleep(random.randint(1,2))
        else:
            print(volume,article_name,'收费章节')