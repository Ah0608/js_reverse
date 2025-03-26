import re
import time

import requests
from loguru import logger
from DrissionPage import ChromiumPage
from src import captcha

cap = captcha.TextSelectCaptcha()


def verify(url):
    content = requests.get(url).content
    # 送入模型识别
    plan = cap.run(content)
    return plan


class BilBil(object):
    def __init__(self):
        self.page = ChromiumPage(9224)
        self.url = "https://passport.bilibili.com/login"

    def get_location(self, element):
        '''
        浏览器屏幕左上角到元素左上角的距离
        '''
        rect = element.rect.screen_location
        center_x = int(rect[0])
        center_y = int(rect[1] - 70)  # 减去70像素，因为顶部有导航栏

        return center_x, center_y

    def bibi(self):
        js_code = """
        var mousePath = [];
        document.body.addEventListener('mousemove', function(event) {
            var x = event.pageX;
            var y = event.pageY;
            mousePath.push({x: x, y: y});

            // 清除旧的轨迹
            if (mousePath.length > 100) {
                mousePath.shift();  // 保留最近的 100 个坐标点
            }

            // 在页面上绘制路径
            var canvas = document.getElementById('mouseCanvas');
            if (!canvas) {
                canvas = document.createElement('canvas');
                canvas.id = 'mouseCanvas';
                canvas.style.position = 'absolute';
                canvas.style.top = 0;
                canvas.style.left = 0;
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                document.body.appendChild(canvas);
            }

            var ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.beginPath();
            ctx.moveTo(mousePath[0].x, mousePath[0].y);
            for (var i = 1; i < mousePath.length; i++) {
                ctx.lineTo(mousePath[i].x, mousePath[i].y);
            }
            ctx.strokeStyle = 'rgba(255, 0, 0, 0.5)';
            ctx.lineWidth = 2;
            ctx.stroke();
        });
        """

        # self.page.run_js(js_code) # 监测鼠标轨迹的js代码
        url = "https://passport.bilibili.com/login"
        self.page.get(url)

        self.page.wait.doc_loaded()
        self.page.ele("x://input[@placeholder='请输入账号']").input('18723561304')
        self.page.ele("x://input[@placeholder='请输入密码']").input('hp200168')
        self.page.ele("x://div[@class='btn_primary ']").click()
        self.page.wait(2)

        captcha_ele = self.page.ele("x://*[@class='geetest_item_wrap']")
        style_value = captcha_ele.attr('style')
        url = re.findall('url\("(.+?)"\);', style_value)[0]
        if url:
            logger.info(url)
            # 送入模型识别
            plan = verify(url)
            logger.info(plan)
            '''
            返回文字坐标： [[119, 174, 193, 244], [223, 189, 298, 267], [87, 69, 158, 140], [31, 196, 109, 275]]
            第一组数据 [119, 174, 193, 244] 表示图像中第一个字矩形区域，左上角为 (119, 174)，右下角为 (193, 244)。
            第二组数据 [223, 189, 298, 267] 表示图像中第二个字矩形区域，左上角 (223, 189)，右下角 (298, 267)。
            第三组数据 [87, 69, 158, 140] 表示图像中第三个字矩形区域，左上角 (87, 69)，右下角 (158, 140)。
            第四组数据 [31, 196, 109, 275] 表示图像中第四个字矩形区域 (31, 196)，右下角 (109, 275)。
            '''
            X, Y = self.get_location(captcha_ele)
            logger.info(f' 浏览器屏幕左上角到元素左上角的距离:{X} {Y}')

            lan_x = 306 / 344 # 前端显示尺寸/原图尺寸
            lan_y = 343 / 384

            for crop in plan:
                x1, y1, x2, y2 = crop

                # 计算矩形的中心点 文字左上角和右下角
                x = (x1 + x2) / 2
                y = (y1 + y2) / 2

                logger.info(f"图片左上角到文字中心点的距离: ({x}, {y})")

                # 计算目标位置（偏移量）
                target_x = int(X + x * lan_x)
                target_y = int(Y + y * lan_y)
                logger.info(f"需要点击的位置: ({target_x}, {target_y})")

                self.page.actions.move_to((target_x, target_y)).click()
                time.sleep(0.5)

            self.page.wait(1)
            self.page.ele("c:div.geetest_commit_tip").click()
        else:
            logger.info("error: 未获得到验证码地址")


if __name__ == '__main__':
    login = BilBil()
    login.bibi()
