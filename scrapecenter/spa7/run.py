import execjs

js_code = open('spa7.js', 'r', encoding='utf-8').read()

player = {
    'name': '凯文-杜兰特',
    'image': 'durant.png',
    'birthday': '1988-09-29',
    'height': '208cm',
    'weight': '108.9KG'
}

ctx = execjs.compile(js_code)
res = ctx.call('getToken', player)
print(res)
