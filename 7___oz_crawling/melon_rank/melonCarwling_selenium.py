import requests, random, json, re, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


# 멜론 차트 접속
url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=header_user)
# html = req.text
# soup = BeautifulSoup(html, "html.parser")

options = Options()
options.add_argument("--headLess")
driver = webdriver.Chrome(options=options)
driver.get(url)
html = driver.page_source
time.sleep(1)
soup = BeautifulSoup(html, "html.parser")
time.sleep(1)

gettime = soup.select_one(".calendar_prid.mt12")
gettimeymd = gettime.select_one(".yyyymmdd").text.strip()
gettimehour = gettime.select_one(".hour").text.strip()
gettime = " 생성시간 : " + gettimeymd + " " + gettimehour

lst_all = soup.find_all(class_=["lst50", "lst100"])

# class="up"
# for rank, x in enumerate(lst_all, 1):
#     a = x.select_one(".up")
#     if a:
#         print("up", a.text)
#         title = x.select_one(".ellipsis.rank01").text.strip()
#         singer = x.select_one(".ellipsis.rank02").text.strip()
#         elbum = x.select_one(".ellipsis.rank03").text.strip()
#         print(f"🔽\n순위 : {rank}\n제목 : {title}\n가수 : {singer}\n앨범 : {elbum}\n")

data = {"datasets": []}
for rank, x in enumerate(lst_all, 1):
    a = x.select_one(".up")
    if a:
        title = x.select_one(".ellipsis.rank01").text.strip()
        singer = x.select_one(".ellipsis.rank02").text.strip()
        elbum = x.select_one(".ellipsis.rank03").text.strip()
        like = x.find("span", class_="cnt").get_text()
        likenum = re.sub("[^0-9]", "", like)
        data["datasets"].append(
            {
                "label": f"{singer} - {title}🔼{a.text}, 순위: {rank}, 좋아요 : {likenum}",
                "data": [
                    {"x": rank, "y": int(a.text), "r": int(likenum)},
                ],
                "borderColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.5)",
                "backgroundColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.5)",
            }
        )


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
