import execjs
import requests

cookies = {
    'NMTID': '00O_DuCXm3HczAaKUkOppNNtFWG1s4AAAGVbpQixg',
    '_iuqxldmzr_': '32',
    '_ntes_nnid': '5ef2a46b6383b9c266668b882127eabf,1741316957425',
    '_ntes_nuid': '5ef2a46b6383b9c266668b882127eabf',
    'WEVNSM': '1.0.0',
    'WNMCID': 'lhzwon.1741316958016.01.0',
    'WM_TID': 'SHeBgNPwJmlBVRVERQOHN3j4x3RKDqix',
    'sDeviceId': 'YD-fkSrmYmHGfVAUxRURQfXZn29xmFeOZdX',
    'ntes_utid': 'tid._.6%252Bkg1BNZpWpFEgEQVRPGc3mpgmEabMMF._.0',
    '__snaker__id': '7sNVvlE6q2BNdIdI',
    'gdxidpyhxdE': '62mhR8KCMfVATQVi2Of5eUIDgOfG1RUkE6BlYA5m2C0Szc041ty1lCOpak7yPgXZglRswbIkc5qQc3jRVWeH6wW%2BJXMlzWKZxhv8xg%2FoJOUuVw218jQx%5CxvsC4gpCPrp%5CyCXH0cjvbVTS1EaHq8Kz4SvJ1VLC%5CS%2BRbnMG4C2BE%2Bi8OVX%3A1741319719118',
    '__csrf': 'f0df1b66b69074cec7ee7e2286ad484c',
    '__remember_me': 'true',
    'MUSIC_U': '002B605FE6F3203F4282C9079FA9B5D42356EAAE0E28F671B2467CD596DA6C754F96D8A71527035DC58A53B799209D562CDF2DDE39C54BEE98C24DBEB691E668C5F917F7018AED87DDE757B6FC6FC8B92F6185725CE11D42E490A7335315077F756A16BDD56681A6C3217DCBD49CD3868CD249911FB962CEB7C3E24636B19EC5F85310C7F108D3585C5B69DD2D8CF98E2379D1580A209399690BE0BF434981D2937CB2410B6EF106C8BD205B64A55A55CFDA9694AF54FD79A4CDECE772DDBE99C46D813D7C49A786E4F1E5CCDAF2A16554987B5566E1F7BD34B6D1843C6FD22A73EA7BC932084A7A36F91DF2B2DDACE3110A665BED07D928F5D05745EE65B1CE583F58DA60C525EE51836622EC93E7C069FEF4C6D6D02FDE20485A5250C0905A4F5D02B9E082C9215EC0A662C9598FBF744EBEE08EB9935823CD2F3874550648FA6B1B931D924A152DD45E27151536A1740FC6EC79725F71A2BFBD0CAD61AC2E7659585589BCD09B2A715995CA88D50DA6',
    'ntes_kaola_ad': '1',
    'WM_NI': 'tohC4k8KQeKv2cwj3fVaOrnORQSjRgvSdxgdHB%2BA2nepghOVki%2F2VGjPZ6gcg0Sl3Hz8vNzxCBqmkz4bNNXeMR6nZrURtSHHS3ZrDNd6xZWogtHzABKIJuuB7YE6TVfZTHQ%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6ee8ee17f919af78fdb6d95bc8ea2c45e839f9fadd742f2af8186ef52fcf5a7bbdb2af0fea7c3b92ab8b1a8a4b761fc959f86ca7ef2bdb98bb26e96bf8193ed45928f9d8bd16db68dac99e6708c9ee5a2b166a7b0a989ce5ea9b7e1d3d54daa9096d7e669a5f09d8db244bae8baaff974819ebf8eea72f8be82afdb6f8f8efa8fd97a978ebcb4cb4491ed9693c746a8eab8bbd665a5ac889bc44a89978696f84af5878bd7d75ea6869ca9d437e2a3',
    'JSESSIONID-WYYY': 'EId9OXSEn%2FJm8YGgSUzdk4MWx4UAnxzqVvM6YBYvBOgk9oRBcpr2lieuR1tnfP4PcqeRz44dTcD1iuHs%5CTcuG1DDHs%5Cp45qx18g0FfG8%2BP5YDOWTR3gadPvsw%2BKjeEqkcxFlj1Yar20Bbohppij7nxG9Uo5UtS5hzlufti2v%2Bn1AJKWR%3A1741575191762',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

params = {
    'csrf_token': 'f0df1b66b69074cec7ee7e2286ad484c',
}

music_id = 2676772689
data = {
    "ids":f"[{music_id}]",
    "level":"standard",
    "encodeType":"aac",
    "csrf_token":"f0df1b66b69074cec7ee7e2286ad484c"
}

with open('params_key.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
encrypt_data = ctx.call('get_params',data)

song_data = response = requests.post(
    'https://music.163.com/weapi/song/enhance/player/url/v1',
    params=params,
    cookies=cookies,
    headers=headers,
    data=encrypt_data,
).json()
song_url = song_data['data'][0]['url']
print(song_url)

content = requests.get(song_url,cookies=cookies, headers=headers).content
with open('song.mp3', 'wb') as f:
    f.write(content)
