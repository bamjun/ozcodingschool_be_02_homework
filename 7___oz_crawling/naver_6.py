import requests
from bs4 import BeautifulSoup


header_user = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}

# 접속하고자 하는 url 입력.

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
# search_url = input("검색어를 입력해주세요 : ")
search_url = "홍삼"

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")


soup.find()  # select_one
soup.find(class_="dsd", text="쇼핑")  # select_one
soup.find()  # select_one
soup.find_all()  # select


soup.find(class_="link_service", text="뉴스")  # select_one
