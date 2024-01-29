import requests
from bs4 import BeautifulSoup


header_user = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}

# 접속하고자 하는 url 입력.
url = "https://www.naver.com/"
req = requests.get(url, headers=header_user)


print(req.request.headers)
