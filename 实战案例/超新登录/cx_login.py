import execjs
from curl_cffi import requests

with open('chaoxinglogin.js', 'r', encoding='utf-8') as f:
    js = f.read()

ctx = execjs.compile(js)
data = ctx.call('get_data','18723561307', 'hp200168')
print(data)
headers = {
    "Connection": "keep-alive",
    "sec-ch-ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"94\"",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.265.400 QQBrowser/12.7.5768.400",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": "https://passport2.chaoxing.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
cookies = {
    "firstReferer": "https://opac.upc.edu.cn:8013/find/sso/login/upc/0",
    "source": "\"\"",
    "JSESSIONID": "B6103D3413274E3E9F1FE7F01B7E5D41",
    "route": "2763694f69e41d34a4f731c4671ac18e",
    "retainlogin": "1"
}
url = "https://passport2.chaoxing.com/fanyalogin"
session = requests.Session()
session.get(url, headers=headers, cookies=cookies, data=data,impersonate='chrome110')

course_data = {
    "courseType": "1",
    "courseFolderId": "0",
    "baseEducation": "0",
    "superstarClass": "",
    "courseFolderSize": "0"
}
res = session.get('https://mooc1-1.chaoxing.com/mooc-ans/visit/courselistdata',impersonate='chrome110',data=course_data)
print(res.text)

