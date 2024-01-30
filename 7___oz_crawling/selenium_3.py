from selenium import webdriver
from bs4 import BeautifulSoup
import requests, time


header_user = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}

# 접속하고자 하는 url 입력.

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
# search_url = input("검색어를 입력해주세요 : ")
search_url = "홍삼"

url = base_url + search_url

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

# 스크롤코드
# driver.execute_script("window.scrollTo(0, 4000)")
# time.sleep(3)

# 스크롤 끝까지 내리기
for x in range(4):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


query = soup.select(".view_wrap")

for num, x in enumerate(query):
    ad = x.select_one(".spview.ico_ad")
    if ad:
        continue

    else:
        title = x.select_one(".title_link._cross_trigger")
        name = x.select_one(".user_info > a")
        tag = title["href"]
        print(f"🔽{num}\n글 제목 : {title.text}\n글 작성자 : {name.text}\n글 링크 : {tag}\n\n")
