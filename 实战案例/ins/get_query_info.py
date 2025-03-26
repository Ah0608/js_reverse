import json

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
    'sessionid': '71076730165%3A3kpvJ7Uv27P68U%3A27%3AAYerdhGTnxjcLh0uS2Ie1woscYk6c-BBeEcMnLddbw',
    'wd': '1920x472',
    'rur': '"EAG\\05471076730165\\0541772070903:01f7b5fdcc69450140acc4dc961d851ecd2964b0af106ca492c95104fbd30bb5ac1dd705"',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,es-ES;q=0.8,es;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/nba/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="130", "Google Chrome";v="130"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-bloks-version-id': '8cfdad7160042d1ecf8a994bb406cbfffb9a769a304d39560d6486a34ea8a53e',
    'x-csrftoken': 'FKXe8evqMRiVFdL2gKIus5Y8voJC58Pw',
    'x-fb-friendly-name': 'PolarisProfilePostsTabContentQuery_connection',
    'x-fb-lsd': 'fVAHRigmOK6mOOTJrpwOpL',
    'x-ig-app-id': '936619743392459',
}

data = {
    'av': '17841471104954591',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': '16',
    '__hs': '20145.HYP:instagram_web_pkg.2.1...1',
    'dpr': '1',
    '__ccg': 'POOR',
    '__rev': '1020394309',
    '__s': 'pqu3cu:23vquu:ecnucd',
    '__hsi': '7475540457622468603',
    '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0DU2wx609vCwjE1EE2Cw8G11wBz81s8hwGxu786a3a1YwBgao6C0Mo2iyo7u3ifK0EUjwGzEaE2iwNwmE7G4-5o4q3y1Sw62wLyESE7i3vwDwHg2ZwrUdUbGwmk0zU8oC1Iwqo5q3e3zhA6bwIxeUnAwCAxW1oxe6UaUaE2xyVrx6',
    '__csr': 'gmhI4n3YQlMX9kJ-DnOR9hd4rl5AhaCTKXiQXWAlPARgBIg5pVbxtWFaQHBDh4-j8WjXHx2i9ZXWHBXqmmiiqQm499JrF4G5FXl4G8CAByp4At2oggGmu74FAiK5FkqtWoG4aBAGq46cDxObBBKi5qjBzHVUijxyl1zDxe6qU01bFr808MBzQ7UN1m2l1Z0ik4h03gizQ1away2qGwXx64E8o6vBypEepK0dow58w25o1Do1y83bu8CLBzothk9Bg4V1t0noFwM4Cmgk0VVUkOyoCbo4mOoMC1kzE6u48dJwnUy1BBwLzQ4JwlA0imE4omhgw0D80jGCS01Enw96E0kcw',
    '__comet_req': '7',
    'fb_dtsg': 'NAcNgr4iy-IU2OrtoIuVJ9-lGIz-ZNtfWutSimzBaqMdlqQO8ttdqXg:17843683126168011:1732862146',
    'jazoest': '26528',
    'lsd': 'fVAHRigmOK6mOOTJrpwOpL',
    '__spin_r': '1020394309',
    '__spin_b': 'trunk',
    '__spin_t': '1740534896',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisProfilePostsTabContentQuery_connection',
    'variables': '{"after":"3574738079282418936_20824486","before":null,"data":{"count":12,"include_reel_media_seen_timestamp":true,"include_relationship_info":true,"latest_besties_reel_media":true,"latest_reel_media":true},"first":12,"last":null,"username":"nba","__relay_internal__pv__PolarisIsLoggedInrelayprovider":true,"__relay_internal__pv__PolarisShareSheetV3relayprovider":false}',
    'server_timestamps': 'true',
    'doc_id': '9278594495553645',
}

proxies = {'http': 'http://192.168.1.186:42018','https': 'http://192.168.1.186:42018'}
response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data,proxies=proxies,impersonate='chrome110')
str_data = response.text


json_data = json.loads(str_data)
for item in json_data["data"]["xdt_api__v1__feed__user_timeline_graphql_connection"]["edges"]:
    code = item["node"]["code"]
    id = item["node"]["id"]
    image_url = item["node"]["image_versions2"]["candidates"][0]["url"]
    print(code, id, image_url)

end_cursor =  json_data["data"]["xdt_api__v1__feed__user_timeline_graphql_connection"]["page_info"]["end_cursor"]
print(f'下一夜的after参数：{end_cursor}')
