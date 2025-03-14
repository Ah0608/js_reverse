import requests
import execjs

with open('apikey.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
x_apikey = ctx.call('getApiKey')

headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "app-type": "web",
    "cache-control": "no-cache",
    "devid": "1e26b15b-d532-4752-ac86-c594ef2c46f3",
    "ok-timestamp": "1740728635540",
    "ok-verify-sign": "y6XKFy3h9Uw+vTflT0OtJgOFRK6amIAcoMF/BddJIhQ=",
    "ok-verify-token": "6e9e4616-eb73-42da-a282-28c2f47c08af",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.oklink.com/zh-hans/btc/tx-list",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "x-apikey": x_apikey,
    "x-cdn": "https://static.oklink.com",
    "x-id-group": "2030107282091440001-c-4",
    "x-locale": "zh_CN",
    "x-site-info": "9FjOikHdpRnblJCLiskTJx0SPJiOiUGZvNmIsICUKJiOi42bpdWZyJye",
    "x-utc": "8",
    "x-zkdex-env": "0"
}
url = "https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict"
params = {
    "offset": "0",
    "limit": "20",
    "t": "1740728635461"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)