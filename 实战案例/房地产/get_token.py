import requests
import execjs

with open("token.js", "r", encoding="utf-8") as f:
    code_js = f.read()

ctx = execjs.compile(code_js)

token = ctx.call("get_token")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://zfcj.gz.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://zfcj.gz.gov.cn/zfcj/fyxx/xkb?sProjectId=930e0442bc60410da837442d9ddb7e02&sPreSellNo=20240005",
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://zfcj.gz.gov.cn/zfcj/fyxx/xmxkbxxView"
data = {
    "sProjectId": "930e0442bc60410da837442d9ddb7e02",
    "token": token,
    "modeID": "1",
    "houseFunctionId": "0",
    "unitType": "",
    "houseStatusId": "0",
    "totalAreaId": "0",
    "inAreaId": "0",
    "buildingId": "63097ed0eb04496b8f9306fc408fe554"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)