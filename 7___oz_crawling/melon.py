import requests
from bs4 import BeautifulSoup


header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 접속하고자 하는 url 입력.

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")
# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")
# lst_all = lst50 + lst100
lst_all = soup.find_all(class_=["lst50", "lst100"])
# time = soup.select(".calendar_prid.mt12")
# timeSET = time.select(".year")[0] + time.select(".hour")[0]
# print(timeSET)

for rank, x in enumerate(lst_all, 1):
    title = x.select_one(".ellipsis.rank01").text.strip()
    singer = x.select_one(".ellipsis.rank02").text.strip()
    elbum = x.select_one(".ellipsis.rank03").text.strip()
    print(f"🔽\n순위 : {rank}\n제목 : {title}\n가수 : {singer}\n앨범 : {elbum}\n")
