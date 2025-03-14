import ddddocr

slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

with open('img_1.png', 'rb') as f:
    bg_data = f.read()

with open('img.png', 'rb') as f:
    sb_data = f.read()

res = slide.slide_match(sb_data, bg_data, simple_target=True)['target'][0]
print(res)