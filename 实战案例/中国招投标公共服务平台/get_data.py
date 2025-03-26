from urllib.parse import urlencode
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import base64
import execjs
import requests


def decrypt_by_des(ciphertext):
    # 确保密钥长度为 8 字节
    key = b"1qaz@wsx"  # 只取前8个字符（DES 需要8字节密钥）

    # 解析 Base64 编码的密文
    ciphertext_bytes = base64.b64decode(ciphertext)

    # 创建 DES 解密器（ECB 模式）
    cipher = DES.new(key, DES.MODE_ECB)

    # 解密并去除填充
    decrypted_data = unpad(cipher.decrypt(ciphertext_bytes), DES.block_size)

    return decrypted_data.decode("utf-8")


cookies = {
    'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2': '1741661654',
    'HMACCOUNT': '9A1A32BD11910290',
    'acw_tc': 'ac11000117417655586192073e00457185321120975013ba271f8d0c974820',
    'Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2': '1741765566',
    'ssxmod_itna': 'iq+xRDyD9ji=DtqGHKGdD7fKoxaC=zYDuG02x05rweGzDAxn40iDtoPNlCr1OnCErqWD52xitKUASRtaoHtR0qWdg=x0aDbqGkbpQxiicDCeDIDWeDiDGb7D=xGYDjAKzCcDm4i7DYqiODlKHShG831h8DQcsDYvFVx0C61xDB1xIHAG4eiDDEAFC8cBsDQKDn=bC1fKD9PoDscDjo4DC2tMPcPvf1So3mP7GDCKDjZv8DmeHpFrkygoPqG+xT0uWbQexwi0q5=0PwA0epQ4iL7tPkqh47+DNeYxlRqDWlDXDD==',
    'ssxmod_itna2': 'iq+xRDyD9ji=DtqGHKGdD7fKoxaC=zYDuG0xn9gPDsvDw24jKG7H4D==',
}
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://ctbpsp.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
url = 'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/1'
params = {
    'province': '',
    'industry': '',
    'type__1017': 'n4+xnDBDgDcDy0DRDxlxGhbCK=0Itq0Qe3teO4D',
}

filtered_params = {k: v for k, v in params.items() if k != 'type__1017'}
query_string = urlencode(filtered_params)
base_url = f"{url}?{query_string}"
print(base_url)

with open('get_params.js','r', encoding='utf-8') as f:
    js = f.read()
ctx = execjs.compile(js)
type__1017 = ctx.call('get_type', base_url)
print(type__1017)

params['type__1017'] = type__1017
response = requests.get(
    url=url,
    params=params,
    cookies=cookies,
    headers=headers,
)
encrypt_text = response.text
print(encrypt_text)

print(decrypt_by_des(encrypt_text))
