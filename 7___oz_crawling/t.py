from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import time

import soupsieve


options = Options()
user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)


url = "https://m2.melon.com/"
driver.get(url)
time.sleep(1)

if driver.current_url != url:
    driver.get(url)
time.sleep(0.6)

driver.find_element(By.LINK_TEXT, "닫기").click()
time.sleep(0.6)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(1)

more_btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
time.sleep(3)  # 노래 하위 50개 불러오는 로딩시간.
soup = BeautifulSoup(driver.page_source, "html.parser")

items = soup.select(".service_list.list_music > .list_item")


num = 1
for i in items:
    title = i.select_one(".title.ellipsis")
    name = i.select_one(".name.ellipsis")

    print(f"순위 : {num}")
    print(f"제목 : {title.text.strip()}")
    print(f"가수 : {name.text.strip()}")
    print()
    num += 1

# driver.quit()


# 순위
# 제목
# 가수이름
# 순위변동


# 과제 목표
# 노래순위
# 노래제목
# 가수이름
# 추가정보
