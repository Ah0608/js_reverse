import execjs
import requests

with open('get_trace_id.js','r',encoding='utf-8') as f:
    js = f.read()
ctx = execjs.compile(js)

cookies = {
    'XSRF-TOKEN': '78INYUTqTyeVAC-d76aWsg',
    '__gc_id': 'e2896bbfd900476ca4fe4d222688ec88',
    '_ga': 'GA1.1.337111831.1742870429',
    '__uuid': '1742870430546.52',
    '__tlog': '1742870430555.89%7C00000000%7C00000000%7C00000000%7C00000000',
    'acw_tc': '2760829a17428704324575075eea7dac0440de21a2409327d1e73b42c98ec2',
    'Hm_lvt_a2647413544f5a04f00da7eee0d5e200': '1742870434',
    'HMACCOUNT': '9A1A32BD11910290',
    'Hm_lpvt_a2647413544f5a04f00da7eee0d5e200': '1742870454',
    '_ga_54YTJKWN86': 'GS1.1.1742870429.1.1.1742870469.0.0.0',
    '__session_seq': '8',
    '__tlg_event_seq': '31',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://www.liepin.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.liepin.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?inputFrom=www_index&workYearCode=0&key=&scene=input&ckId=cei1lxwcgvjwp0v613z0tdqvn0ziea1b&dq="}',
    'X-Fscp-Fe-Version': '',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': 'd745047f-12e7-4db9-8bda-8466e95ceaa2',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': '78INYUTqTyeVAC-d76aWsg',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

headers['X-Fscp-Trace-Id'] = ctx.call('w')

json_data = {
    'data': {
        'mainSearchPcConditionForm': {
            'city': '410',
            'dq': '410',
            'currentPage': 1,
            'pageSize': 40,
            'key': '',
            'suggestTag': '',
            'workYearCode': '0',
            'compId': '',
            'compName': '',
            'compTag': '',
            'industry': '',
            'salaryCode': '',
            'jobKind': '',
            'compScale': '',
            'compKind': '',
            'compStage': '',
            'eduLevel': '',
            'salaryLow': '',
            'salaryHigh': '',
            'hrActiveTimeCode': '',
        },
        'passThroughForm': {
            'skId': 'f00bdt2c9chjmwlm625pmz755v7qy9g8',
            'fkId': 'f00bdt2c9chjmwlm625pmz755v7qy9g8',
            'sfrom': 'search_job_pc',
            'scene': 'page',
            'ckId': 'a9qrkm6mba3yci20stlzl877m1agcyob',
        },
    },
}

response = requests.post(
    'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.json())