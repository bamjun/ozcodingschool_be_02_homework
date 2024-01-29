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


query = soup.select(".view_wrap")

for x in query:
    ad = x.select_one(".spview.ico_ad")
    if ad:
        continue

    else:
        title = x.select_one(".title_link._cross_trigger")
        name = x.select_one(".user_info > a")
        tag = title["href"]
        print(f"🔽\n글 제목 : {title.text}\n글 작성자 : {name.text}\n글 링크 : {tag}\n\n")
