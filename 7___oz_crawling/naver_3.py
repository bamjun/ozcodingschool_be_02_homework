import requests
from bs4 import BeautifulSoup


header_user = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}

# 접속하고자 하는 url 입력.

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
# search_url = input("검색어를 입력해주세요 : ")
search_url = "손흥민"

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")
query = soup.select(".news_tit")

keyword_box = soup.select(".keyword_box_wrap.type_color")


for i in keyword_box:
    name = i.select_one(".name.elss")
    category = i.select_one(".etc_area")
    title = i.select_one(".title_link._cross_trigger._foryou_trigger")
    print(f"블로그 작성자는 : {name.text}")
    print(f"분야 : {category.text}")
    print(f"제목 : {title.text}")
    print()
