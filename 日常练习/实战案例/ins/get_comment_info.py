import pprint

from curl_cffi import requests

cookies = {
    'ig_did': '228BB3AC-6CC5-4319-A86D-51BA61AFDE78',
    'ps_l': '1',
    'ps_n': '1',
    'datr': 'U1tJZ1r387ECVoLlCGLh_hMv',
    'mid': 'Z0lfsAALAAFeOzmmY1JOoEDkgQNm',
    'ig_nrcb': '1',
    'csrftoken': 'FKXe8evqMRiVFdL2gKIus5Y8voJC58Pw',
    'ds_user_id': '71076730165',
    'sessionid': '71076730165%3A3kpvJ7Uv27P68U%3A27%3AAYc2H8wA3q4UEYNcGwu0JFa-D2Tdiy3zLP0zVjv1AA',
    'wd': '1920x537',
    'rur': '"EAG\\05471076730165\\0541772082843:01f79883a34b01bc8ed77990184552f7a3c94677524d06325851f73af9038421bce53819"',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,es-ES;q=0.8,es;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/p/DGKRMGPs-iq/?img_index=1',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="130", "Google Chrome";v="130"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-csrftoken': 'FKXe8evqMRiVFdL2gKIus5Y8voJC58Pw',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR0HqiqEqF3XwgbODCDNOL_Y7_BC6aT5ZvHz_Yg87bQClDWI',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-session-id': '3e53r3:23vquu:509r4r',
}

params = {
    'can_support_threading': 'true',
    'min_id': '{"cached_comments_cursor": "18025531139352278", "bifilter_token": "KHkA5QU22nwZQADFUN2YHBVAAAiCjDFME0AACT48xo5tPwC8c7Hbx8o_AGtVp7JrU0EAKjiVj-owQADKEd02vjBAABF3bmieBUEA0lYKJ0qXPwB4D7PPVwdAALijQRUHH0AAW2a05ZQhQAB8DteRGktAAD-zsgSzMkAAAA=="}',
    'sort_order': 'popular',
}

proxies = {'http': 'http://192.168.1.186:42018','https': 'http://192.168.1.186:42018'}

response = requests.get(
    'https://www.instagram.com/api/v1/media/3569741252774848682/comments/',
    params=params,
    cookies=cookies,
    headers=headers,
    proxies=proxies,
    impersonate='chrome110'
)

comments_data = response.json()
for item in comments_data["comments"]:
    comments_dict = dict()
    comments_dict['用户id'] = item["user_id"]
    comments_dict['评论id'] = item["pk"]
    comments_dict['评论内容'] = item["text"]
    comments_dict['评论用户名'] = item["user"]["username"]
    pprint.pprint(comments_dict)


next_min_id = comments_data["next_min_id"]
print(f'评论下一页的参数为：{next_min_id}')