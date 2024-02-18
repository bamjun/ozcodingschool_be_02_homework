import time, re, pymysql
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By






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

link_list = []
updown_list = []
rank_list = []
for x in range(1, 6):
    print("*"*10, f'현재 {x} 페이지 수집 중 입니다.', '*'*10)
    url = f'https://product.kyobobook.co.kr/bestseller/online?period=001&dsplDvsnCode=001&dsplTrgtDvsnCode=002&saleCmdtDsplDvsnCode=TOT&page={x}'
    
    browser.get(url)


    try:
        inputDate = browser.find_element(By.CSS_SELECTOR, '#baseDateText').text
        match = re.search(r'(\d+)년 (\d+)월 (\d+)일', inputDate)
        year, month, day = match.groups()
        data_obj = datetime(int(year), int(month), int(day))
        inputDate = data_obj.strftime("%Y-%m-%d")
    except Exception as e:
        print(e)

    
    datas = browser.find_elements(By.CLASS_NAME, 'prod_item')
    datas = datas
    for j in range(len(datas)):
        i = datas[j]
        link = i.find_element(By.CLASS_NAME, 'auto_overflow_inner a.prod_info').get_attribute('href')
        link_list.append(link)
        updown = i.find_element(By.CSS_SELECTOR, '.rank_status').text.split('\n급상승')[0]
        if updown == '' or updown == 'NEW':
            updown = '0'
        updown_list.append(updown)
        rank = i.find_element(By.CSS_SELECTOR, '.badge_flag').text
        if rank == '':
            rank = str((j+1)+((x-1)*20))
        rank_list.append(rank)
    time.sleep(3)


conn = pymysql.connect(
    host='localhost',
    user='root',
    password= '1Qjawnsdl!',
    db = 'booksminiproject',
    cursorclass = pymysql.cursors.DictCursor
)
index_range = 0
with conn.cursor() as cur:
    for x in range(len(link_list)):
        link = link_list[x]
        max_attempts = 2
        attempts = 0

        # inputDate = datetime.now().strftime('%Y-%m-%d')
        kyoboRank = rank_list[x]

        check_sql = "SELECT COUNT(*) AS a FROM kyobo_ranking WHERE inputdate = %s and kyoborank = %s"
        cur.execute(check_sql, (inputDate, kyoboRank))
        result = cur.fetchone()
        if result['a'] != 0:
            continue

        while attempts < max_attempts:
            try:
                browser.get(link)

                title = browser.find_element(By.CLASS_NAME, 'prod_title').text
                author = browser.find_element(By.CLASS_NAME, 'author').text

                a_element = browser.find_element(By.CSS_SELECTOR, 'div.prod_info_text.publish_date a.btn_publish_link')
                publisher = a_element.text

                # <div> 태그 안의 텍스트 추출 (전체 div의 텍스트에서 <a> 태그의 텍스트를 제외한 나머지)
                div_element = browser.find_element(By.CSS_SELECTOR, 'div.prod_info_text.publish_date')
                # <a> 태그의 텍스트와 " · " 문자열을 제거하여 최종 텍스트 추출
                publishing = div_element.text.replace(publisher, '').replace(' · ', '').strip()
                match = re.search(r'(\d+)년 (\d+)월 (\d+)일', publishing)
                year, month, day = match.groups()
                data_obj = datetime(int(year), int(month), int(day))
                publishing = data_obj.strftime("%Y-%m-%d")

                

                isbn = browser.find_element(By.CSS_SELECTOR, '.tbl_row tbody tr td').text


                kyoboRating = browser.find_element(By.CSS_SELECTOR, '.caption-badge.caption-secondary span.val').text
                if kyoboRating == '':
                    kyoboRating = 0


                text = browser.find_element(By.CSS_SELECTOR, '.product_detail_area.klover_review_wrap p.title_heading').text
                review = re.findall(r'\((\d+)\)', text.replace(',',''))
                # 첫 번째 매칭된 숫자만 추출 (문자열 리스트에서 첫 번째 요소를 정수로 변환)
                kyoboReview = int(review[0]) if review else None



                price = browser.find_element(By.CSS_SELECTOR, '.sale_price s.val').text[:-1]
                kyoboPrice = int(price.replace(',', '').strip())

                
                price = browser.find_element(By.CSS_SELECTOR, '.prod_price span.price span.val').text[:-1]
                kyoboSalePrice = int(price.replace(',', '').strip())

                point = browser.find_element(By.CSS_SELECTOR, '.point_text').text[:-1]
                kyoboPoint = int(point.replace(',', '').strip())

                # cover_url,isbn,input_date,title,author,publisher,publishing,rating,review,price,ranking,salePrice,point

                coverUrl = browser.find_element(By.CSS_SELECTOR, '.portrait_img_box.portrait img').get_attribute('src')

                break  # try 블록이 성공적으로 실행되면 반복문 종료
            except Exception as e:
                print(f"오류 발생: {e}")
                attempts += 1
                with open('error_log.txt', 'a') as file:  # 'a' 모드는 파일에 내용을 추가합니다.
                    file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {link} - 오류 발생({attempts}번째 시도): {e}\n")
                if attempts == max_attempts:
                    print("재시도 실패. 프로그램을 종료합니다.")
                else:
                    print(f"{attempts}번째 재시도 중...")
                    time.sleep(2)







        # ISBN이 테이블에 존재하는지 확인하는 SQL 쿼리
        check_sql = "SELECT COUNT(*) AS a FROM books WHERE isbn = %s"

        # 새 데이터를 삽입하는 SQL 쿼리
        insert_sql = """INSERT INTO books(isbn, title, author, publisher, publishing, coverurl)
                        VALUES(%s, %s, %s, %s, %s, %s)"""

        # ISBN 존재 여부 확인
        cur.execute(check_sql, (isbn))

        result = cur.fetchone()

        # result[0]은 COUNT(*)의 결과, 즉 매칭되는 행의 수를 나타냅니다.
        if result['a'] == 0:
            # ISBN이 테이블에 존재하지 않으므로 새 레코드 삽입
            cur.execute(insert_sql, (isbn, title, author, publisher, publishing, coverUrl))
            print("새로운 레코드가 삽입되었습니다.")
        else:
            print("이미 존재하는 ISBN입니다. 삽입하지 않습니다.")


        

        # ISBN이 테이블에 존재하는지 확인하는 SQL 쿼리
        check_sql = "SELECT COUNT(*) AS a FROM kyobo_ranking WHERE inputdate = %s and isbn = %s;"

        # ISBN 존재 여부 확인
        cur.execute(check_sql, (inputDate, isbn))
        result = cur.fetchone()

        # result[0]은 COUNT(*)의 결과, 즉 매칭되는 행의 수를 나타냅니다.
        if result['a'] != 0:
            print("RANK이미 존재하는 ISBN입니다. 삽입하지 않습니다.")
            continue
            


        sql = """INSERT INTO kyobo_price(
            isbn,inputdate,kyoboprice,kyobosaleprice,kyobopoint, kyobourl
            )
            VALUES(
                %s,%s,%s,%s,%s,%s
            )
            """
        cur.execute(sql, (isbn,inputDate,kyoboPrice,kyoboSalePrice,kyoboPoint, link))


        sql = """INSERT INTO kyobo_ranking(
            isbn,inputdate,kyoborank,kyoborating,kyoboreview, kyoboupdown
            )
            VALUES(
                %s,%s,%s,%s,%s,%s
            )
            """
        cur.execute(sql, (isbn,inputDate,kyoboRank,kyoboRating,kyoboReview, updown_list[x]))


        conn.commit()
        time.sleep(2)
        
        index_range += 1
        if index_range == 10:
            index_range = 0
            browser.quit()
            time.sleep(10)
            
            user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"


            chrome_driver_path = '/usr/bin/chromedriver'
            service = Service(executable_path=chrome_driver_path)

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")  # GUI 없이 실행
            chrome_options.add_argument("--no-sandbox")  # Sandbox 프로세스 사용 안 함
            chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 사용 안 함
            chrome_options.add_argument(f"User-Agent={user}")
            ChromeDriverManager().install()
            browser = webdriver.Chrome(service=service, options=chrome_options)
            

            
        
        

conn.close()