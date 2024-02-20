import pymysql, pass1, time, re, platform
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium import webdriver

# 로컬환경의 윈도우와 서버 환경 리눅스에서 시작하는 코드 구분.  
if platform.system() == 'Windows':
    ChromeDriverManager().install()
    browser = webdriver.Chrome()
else:
    user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

    chrome_driver_path = '/usr/bin/chromedriver'
    service = Service(executable_path=chrome_driver_path)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # GUI 없이 실행
    chrome_options.add_argument("--no-sandbox")  # Sandbox 프로세스 사용 안 함
    chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 사용 안 함
    chrome_options.add_argument(f"User-Agent={user}")
    # Chrome 실행 파일의 경로를 지정해야 할 경우, 아래 옵션을 사용
    # chrome_options.binary_location = '/path/to/google-chrome'
    ChromeDriverManager().install()
    browser = webdriver.Chrome(service=service, options=chrome_options)

conn = pymysql.connect(
    host='localhost',
    user='root',
    password= pass1.password(),
    db = 'booksminiproject',
    cursorclass = pymysql.cursors.DictCursor
)

link_list = []
with conn.cursor() as cur:

    sql = 'SELECT books.isbn, (SELECT kyobourl FROM kyobo_price WHERE kyobo_price.isbn = books.isbn LIMIT 1) AS kyobourl FROM books JOIN kyobo_price ON books.isbn = kyobo_price.isbn where books.category is null GROUP BY books.isbn'
    cur.execute(sql)
    result = cur.fetchall()
    
    for x in result:
        link_list.append(str(x['kyobourl']))


    for x in result:
        try:
            browser.get(x['kyobourl'])

            category = browser.find_elements(By.CLASS_NAME, 'breadcrumb_item')

            if category[1].text == '국내도서':
                category = f"{category[2].text}"
            else:
                category = f"{category[1].text} - {category[2].text}"

            print(x['isbn'], category)
            
            sql = 'UPDATE books SET category = %s WHERE isbn = %s'
            cur.execute(sql, (category, x['isbn']))

            conn.commit()

            time.sleep(2)
        except Exception as e:
            print(e)