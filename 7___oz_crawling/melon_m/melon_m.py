from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time, re, json
from datetime import datetime

options = Options()
# 창안띄우고 크롤링
# options.add_argument("--headLess")

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

url = "https://m2.melon.com/index.htm"
driver.get(url)

# url_current = driver.current_url
# print(url_current)


time.sleep(1)
if driver.current_url != url:
    driver.get(url)
    time.sleep(0.5)

driver.find_element(By.LINK_TEXT, "닫기").click()
time.sleep(0.2)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(0.2)

more_btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
time.sleep(1)
soup = BeautifulSoup(driver.page_source, "html.parser")


items = soup.select(".service_list.list_music > .list_item")


data = []
for num, i in enumerate(items, 1):
    title = i.select_one(".title.ellipsis")
    name = i.select_one(".name.ellipsis")
    image = re.search(r"url\(['\"]?(.*?)['\"]?\)", i.select_one(".img")["style"])
    image = image.group(1)
    updown = i.select_one(".rankimg_updown").text.strip()

    print(updown)
    print(image)

    data.append(
        {
            "image": image,
            "rank": num,
            "updown": updown,
            "title": title.text.strip(),
            "singer": name.text.strip(),
        }
    )
    print(f"순위 : {num}")
    print(f"제목 : {title.text.strip()}")
    print(f"가수 : {name.text.strip()}")
    # print(f" : {}")
    print()

driver.quit()


gettime = "멜론 순위" + str(datetime.now())
# 파일로 저장
with open("data.js", "w", encoding="utf-8") as file:
    file.write(
        "const data = "
        + json.dumps(data, indent=2, ensure_ascii=False)
        + "; \n\nconst crawltime = "
        + json.dumps(gettime, indent=2, ensure_ascii=False)
        + ";"
    )

print("JavaScript 파일이 생성되었습니다.")


# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, ".img-logo").click()
# time.sleep(0.5)
# driver.find_element(By.CSS_SELECTOR, ".banner_full_close").click()
# time.sleep(0.5)
# nav_items = driver.find_elements(By.CSS_SELECTOR, ".nav_item")
# nav_items[2].click()
# slee = ".service_list_more.noline.sprite.hide"
# morre = driver.find_elements(By.CSS_SELECTOR, slee)
# morre[1].click()


# 과제 목표
# 노래순위
# 노래제목
# 가수이름
# 추가정보
