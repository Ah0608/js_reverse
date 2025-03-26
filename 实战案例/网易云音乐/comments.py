import requests
import execjs

cookies = {
    'NMTID': '00O_DuCXm3HczAaKUkOppNNtFWG1s4AAAGVbpQixg',
    '_iuqxldmzr_': '32',
    '_ntes_nnid': '5ef2a46b6383b9c266668b882127eabf,1741316957425',
    '_ntes_nuid': '5ef2a46b6383b9c266668b882127eabf',
    'WEVNSM': '1.0.0',
    'WNMCID': 'lhzwon.1741316958016.01.0',
    'WM_NI': 'RrGKkN3qLYopil7FgJA4BcBw8B1qvBywXMcCY6G4obu2QWGlV%2BXks8RYcDLOAX9BQLVPR1B%2BCBsXT4AjOAr8w1f3LU5DygRfCDitbhCqgOdz2%2FiYKOPyWaMgi1wQ%2FI6BTGg%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeace43e98bd9c94d56b90ac8fa3d45e828e9aaccb46abb7bcd1ec5fa68de1d3ea2af0fea7c3b92a92ae89acea46f1af84baee7cabb4f9a7e64283ec8e84c17dfc9eff92f54abba998aee2499bea89d5ee6ab7ee9fb8c66896f5988cf2349287ada5cf458388f7a3d44896909ed2c121819ebdb9d74083b681a2f134b5efaad4cf5ff79cb788d16e819ca795e16481afa9b0e772f2f1a7baca4594a79982d06dabefb9b2ae43f69e9ca8e637e2a3',
    'WM_TID': 'SHeBgNPwJmlBVRVERQOHN3j4x3RKDqix',
    'sDeviceId': 'YD-fkSrmYmHGfVAUxRURQfXZn29xmFeOZdX',
    'ntes_utid': 'tid._.6%252Bkg1BNZpWpFEgEQVRPGc3mpgmEabMMF._.0',
    '__snaker__id': '7sNVvlE6q2BNdIdI',
    'gdxidpyhxdE': '62mhR8KCMfVATQVi2Of5eUIDgOfG1RUkE6BlYA5m2C0Szc041ty1lCOpak7yPgXZglRswbIkc5qQc3jRVWeH6wW%2BJXMlzWKZxhv8xg%2FoJOUuVw218jQx%5CxvsC4gpCPrp%5CyCXH0cjvbVTS1EaHq8Kz4SvJ1VLC%5CS%2BRbnMG4C2BE%2Bi8OVX%3A1741319719118',
    '__csrf': 'f0df1b66b69074cec7ee7e2286ad484c',
    '__remember_me': 'true',
    'MUSIC_U': '002B605FE6F3203F4282C9079FA9B5D42356EAAE0E28F671B2467CD596DA6C754F96D8A71527035DC58A53B799209D562CDF2DDE39C54BEE98C24DBEB691E668C5F917F7018AED87DDE757B6FC6FC8B92F6185725CE11D42E490A7335315077F756A16BDD56681A6C3217DCBD49CD3868CD249911FB962CEB7C3E24636B19EC5F85310C7F108D3585C5B69DD2D8CF98E2379D1580A209399690BE0BF434981D2937CB2410B6EF106C8BD205B64A55A55CFDA9694AF54FD79A4CDECE772DDBE99C46D813D7C49A786E4F1E5CCDAF2A16554987B5566E1F7BD34B6D1843C6FD22A73EA7BC932084A7A36F91DF2B2DDACE3110A665BED07D928F5D05745EE65B1CE583F58DA60C525EE51836622EC93E7C069FEF4C6D6D02FDE20485A5250C0905A4F5D02B9E082C9215EC0A662C9598FBF744EBEE08EB9935823CD2F3874550648FA6B1B931D924A152DD45E27151536A1740FC6EC79725F71A2BFBD0CAD61AC2E7659585589BCD09B2A715995CA88D50DA6',
    'ntes_kaola_ad': '1',
    'JSESSIONID-WYYY': 'P38I04msaH7UUNKBD6mCfj%5CxEYpmVuj2NS6TOIXpJntpsMKOPOVqsF%2FMihHT%2BUF7TdGgQ1H2u1jl13QuiUOWoBGu0P%2BOAMJ%5CTgXqSKkd%2FrQzESUsdOPW%2FviAlwY1HJdS4kXxyH6ciBAln%2BWlZGpABDtDKUYn61b0wxw%5CjG%2FXXbdyCziM%3A1741337463859',
}
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'nm-gcore-status': '1',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://music.163.com/search/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}
url = "https://music.163.com/weapi/comment/resource/comments/get"
params = {
    "csrf_token": "f0df1b66b69074cec7ee7e2286ad484c"
}
data = {
    "rid": "A_PL_0_991319590",
    "threadId": "A_PL_0_991319590",
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": "f0df1b66b69074cec7ee7e2286ad484c"
}
encrypt_data = execjs.compile(open("params_key.js", encoding='utf-8').read()).call("get_params",data)

response = requests.post(url, headers=headers, cookies=cookies, params=params, data=encrypt_data)
print(response.text)