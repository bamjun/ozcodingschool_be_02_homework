import requests
from bs4 import BeautifulSoup


# 접속하고자 하는 주소 입력 => url
url = "https://www.naver.com/"

# get 방식을 이용해서 서버에게 Resource(자원 = .html, .css, .js 파일)을 보내도록 요청한다. 데이터 수신이 가능하게 준비한다.
# requests 의 경우 거의 처음에 사용되고 이후에는 잘 사용되지 않음, 왜냐면 정적인 사이트에서는 HTML 코드가 변하지 않기 때문이다.
# requests로넘어노느 내용은 예를들어 네이버에 화면에서 마우스 오른쪽 버튼을 누르고페이지 소스보기로 보이는 내용과 동일하다.
req = requests.get(url)

# get 방식을 통해서 가저온 많은 데이터 중 우리가 필요한건 텍스트 형태의 자료다.(가장 중효한 html 포함되어 있다.)
html = req.text

# BeautifulSoup이라는 함수에는 2가지 파라미터를 넣는데, html, "html.parser" 넣는다.
# 넣으면 파서(컴퓨터가 이해할 수 있도록 html 분해해서 트리구조로 변경하는 것)가 진행된다.
soup = BeautifulSoup(html, "html.parser")

# select_one 원하는 태그를 찾을 수 있는데 기준은 클래스명, id 태그도 가능하다. 클래스 경우는 앞에 점(.), id는 앞에 #을 붙인다.
query = soup.select_one("#query")
print(query)
