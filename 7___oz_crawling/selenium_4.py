from selenium import webdriver
import requests, time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()

user = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"


options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
# 주소줄 바로 밑에 자동 실행중 나오는거 없애는거.
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# options.add_argument("--start-maximized")
# options.add_argument("--start-fullscreen")
# options.add_argument("window-size=500, 500")

# 브라우저 화면이 나오지 않은 상태에서 크롤링
# options.add_argument("--headLess")

# 오디오 음소거
# options.add_argument("--mute-audio")
# 시크릿 모드
options.add_argument("incognito")


driver = webdriver.Chrome(options=options)
url = "https://www.naver.com/"
driver.get(url)
