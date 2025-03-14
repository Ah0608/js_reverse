import subprocess
from loguru import logger


def download_video(v_link, v_path):
    command = rf'yt-dlp --proxy "http://192.168.1.186:42018" --cookies cookies.txt -f "bestvideo+bestaudio" -o "{v_path}" {v_link}'
    try:
        subprocess.run(command, check=True, shell=True)
        logger.info('视频下载成功！---- {}'.format(v_path))
    except subprocess.CalledProcessError as e:
        logger.info(f"Error occurred: {e}")


v_link = 'https://www.instagram.com/p/DGhQJoROnwM/'
v_path = r'D:\workfile\PycharmProjects\spider_study\日常练习\实战案例\ins\ins.mp4'
download_video(v_link,v_path)