import json

from curl_cffi import requests
import execjs


def get_note_data(note_id):
    return {"source_note_id": note_id, "image_scenes": ["CRD_PRV_WEBP", "CRD_WM_WEBP"]}


cookies = {
    'gid': 'yYf44Wq0Sq0qyYf44WqjiJF0iJyS464U8xCTE2WvIAK9v728q6k8d9888yq48WW8dKyqdJqJ',
    'web_session': '040069b56113ab6ae3bb738e49354ba3e14e8d',
    'abRequestId': 'e8515eba-228e-5039-b38b-db4edd55a6ed',
    'webBuild': '4.55.1',
    'a1': '194d4a2946arg36bgidwnnld914io3hq3n6bs0k0z50000220077',
    'webId': 'e4e8bd6fb03b06da024ecba1a4827988',
    'x-user-id-creator.xiaohongshu.com': '641550e3000000000e00b3ed',
    'customerClientId': '992458977974440',
    'customer-sso-sid': '68c51746780659448498773727371959cdd3160c',
    'access-token-creator.xiaohongshu.com': 'customer.creator.AT-68c517467806598778483974obj8sujdinjnjjss',
    'galaxy_creator_session_id': 'DI3ofTfuK432jXUMeWTB0FFtIhVF4lAjvXOB',
    'galaxy.creator.beaker.session.id': '1738734217031037633638',
    'xsecappid': 'xhs-pc-web',
    'acw_tc': '0a4ab81817392550140755109e1a30020145fb509d1bc29d0240608fcc4eb7',
    'unread': '{%22ub%22:%2267a72f81000000001800d566%22%2C%22ue%22:%2267a76e790000000028034b0f%22%2C%22uc%22:25}',
    'websectiga': '6169c1e84f393779a5f7de7303038f3b47a78e47be716e7bec57ccce17d45f99',
    'sec_poison_id': 'c6e4230c-3b7b-48cf-8f9f-6cc6d609c7c2',
}

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.xiaohongshu.com',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.467.400 QQBrowser/13.4.6232.400',
    'x-b3-traceid': '8fd7b97f1753ef3b',
    'x-mns': 'awjO85jEOhbvFidKigmvNHFM+DNmGv/f6WpcvfNve7YhFuHb3ZQPw+l+39Z6BBnOuuOSeoYEdNYRYmi8nB+3Z3J7xGPY47SF9aFCJR4NG7alBp0QP23gdvoLtnmJJz7TDYjdBdX2l6EDykPNZIKz64xt8CxYJQ3dh5vOW7HfWdmKGzpBnv/1JmOggm0mFQy3kRhh6boH3ZPIoT0PpTN1DeYkZQxMJnE+NwLIGfHMagkbXhLgQkuuRv8BfLghpgjcm+bC4p5YhBLEONB/bjS6WjJQtnjD1GEeSlldxxEjy/Jp+R3RHzQIlDB+4wXSdfWlGYcoN6TgzWQpWTJNB5Y38a07j2OzS1yjFMKgK1MeLJTiGHN4a78G0fxhIuF8TPu51PWd0ZTflEfjJYSWiC8XO/TgLLfPGR0het32pKQxkzeZn1ZoXuPgXjug00p7dntZpWo15kxNXD9zXXO9H2ScH5C0ulJIL7BTPuPSBEXXScX5lvWJbgabNmxeW6ID9dB5mB',
    'x-s': 'XYW_eyJzaWduU3ZuIjoiNTYiLCJzaWduVHlwZSI6IngyIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImRlOGFjMGE0MmFmMDFiNTkxMDhkYWNjMTI1ZmIyMzNlN2UzNWE1MTU0NzRlZDRhOWM0MWNjNWE1NDQ3NDhiNWQxN2M0YWYwZDVmZDFlZWVmZjhkMjM2OGEwMTBkZDc1MjNiMjk1NjQxOTdmMzY5NjExODBjOTg4YzZmZDdlOGVkMzk2NjVlZWQwOTYyZjljYzk5NjQxZDFlMzgxOTBmZjRiYTBhZTZhMTdkZmE1YWNkNzNhODJkZGI4Yzc3MzU0NmUxYjdhY2NhM2MxMzJjYWYyY2Y3NTg0MTIwN2Y2MzBmYmEzM2Q2OGM1MTY2YjM3YWQzZDBmMzM5MjE0ZDVhMzViYmFmNzE4MGJiNGUyNTZkNDE3OTY0YjE5OWQwNDJlODkyNDVlNTE3NTNkNWE5ZDljNDRjZWI5ZDgzNWFmYWNjMDAzN2UyMDg4ZThlN2E0OWRiZDAzNTViOTgzYWZhNTlkMWI3MjYwMTBhNjcwYzAzZmQzYjI4YzU5NjQ5NDc1YTU1Mjg4ZDc1ZDg2MzFhYWI5YzA3ZTk1MDk1MjkyMTRmIn0=',
    'x-s-common': '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',
    'x-t': '1739256800248',
    'x-xray-traceid': 'ca79e45147e2169d7eb0fc39714981ed',
}


def main(note_id):
    json_data = {
        'source_note_id': note_id,
        'image_formats': [
            'jpg',
            'webp',
            'avif',
        ],
        'extra': {
            'need_body_topic': '1',
        },
        'xsec_source': 'pc_user',
        'xsec_token': 'ABzI5oAzxr3ybU9jw0sSN5ruU2JCPfNRGnlJknq1IW8JA=',
    }

    data = get_note_data(note_id)
    with open('xhs.js', 'r', encoding='utf-8') as f:
        js_code = f.read()

    ctx = execjs.compile(js_code)
    res = ctx.call('get_xs', '/api/sns/web/v1/feed', json.dumps(json_data), cookies['a1'])
    xs = res['X-s']
    xt = res['X-t']
    print('xs-----',xs)
    print('xt-----',xt)
    headers['x-s'] = xs
    headers['x-t'] = str(xt)
    response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/feed', cookies=cookies, headers=headers,
                             json=json_data, impersonate='chrome110')

    print(response.json())


if __name__ == '__main__':
    note_id = '67376468000000001a01de43'
    main(note_id)