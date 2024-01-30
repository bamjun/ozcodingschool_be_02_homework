# 배운내용

import requests  
from bs4 import BeautifulSoup  
requests 와 bs4 를 활용해서, 크롤링 하기.

# naver_1.py

<img src="images/naver1.png">  
  
# naver_2.py  
  
  <img src="images/naver2.png">

# naver_3.py

  <img src="images/naver3.png">

# naver_4.py

  <img src="images/naver4.png">

# naver_5.py

  <img src="images/naver5.png">

# naver_6.py

find = select_one
find_all = select

# melon.py

  <img src="images/melon.png">

# selenuum

- win의 경우 아래 명령어로 크롬 드라이버 매니저 설치  
  pip install webdriver-manager
- 아래 명령어로 셀레니움 설치  
  pip install selenium
- 셀레니움에 기능 추가하기,  
  from selenium.webdriver.chrome.options import Options  
  창크기나, 주소표시줄 바로 밑, 자동실행문 문구, 창크기등 크롬 브라우저 관련설정.  
  from selenium.webdriver.common.by import By  
   driver.find_element(By.CSS_SELECTOR, classText).send_keys(Keys.ENTER)  
   from selenium.webdriver.common.keys import Keys  
   셀레니움에서 키 입력관련.

  # melon_rank

  멜론 차트 데이터 크롤링해서, 버블 차트 만들기  
  <img src="images/melonRankMain.png">
