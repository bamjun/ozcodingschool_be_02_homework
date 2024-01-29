import requests
from bs4 import BeautifulSoup


header_user = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}

# 접속하고자 하는 url 입력.

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
# search_url = input("검색어를 입력해주세요 : ")
search_url = "손흥민"

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")


# query = soup.select(".view_wrap")

# for x in query:
#     name = x.select_one(".name")
#     title = x.select_one(".title_link._cross_trigger")
#     content = x.select_one(".dsc_link._cross_trigger")
#     print(f"작성자 : {name.text}")
#     print(f"제목 : {title.text}")
#     print(f"내용 : {content.text}\n")

title = soup.select(".title_link._cross_trigger")
name = soup.select(".user_info > a")  # > : 바로 다음에 오는 태그를 선택할때 사용할 수 있음.

for i in zip(title, name):
    print("블로그 글 제목 : ", i[0].text)
    print("블로그 작성자 : ", i[1].text)
    print("블로그 링크 : ", i[0]["href"])
    print()
