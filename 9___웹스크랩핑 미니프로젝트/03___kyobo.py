
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pymysql, pass1, time, re
from datetime import datetime
from selenium import webdriver



ChromeDriverManager().install()
browser = webdriver.Chrome()

url = 'https://product.kyobobook.co.kr/bestseller/online?period=001&page=1'
browser.get(url)


link_list = []
for x in range(1, 2):
    print("*"*10, f'현재 {x} 페이지 수집 중 입니다.', '*'*10)
    url = f'https://product.kyobobook.co.kr/bestseller/online?period=001&dsplDvsnCode=001&dsplTrgtDvsnCode=002&saleCmdtDsplDvsnCode=TOT&page={x}'
    
    browser.get(url)

    datas = browser.find_elements(By.CLASS_NAME, 'auto_overflow_inner a.prod_info')
    datas = datas
    for i in datas:
        link = i.get_attribute('href')
        link_list.append(link)
    time.sleep(3)



conn = pymysql.connect(
    host='localhost',
    user='root',
    password= pass1.password(),
    db = 'booksminiproject',
    cursorclass = pymysql.cursors.DictCursor
)

with conn.cursor() as cur:

    for link in link_list:
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

        inputDate = datetime.now().strftime('%Y-%m-%d')

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

        kyoboRank = browser.find_element(By.CSS_SELECTOR, '.prod_best_text span.rank').text

        price = browser.find_element(By.CSS_SELECTOR, '.prod_price span.price span.val').text[:-1]
        kyoboSalePrice = int(price.replace(',', '').strip())

        point = browser.find_element(By.CSS_SELECTOR, '.point_text').text[:-1]
        kyoboPoint = int(point.replace(',', '').strip())

        # cover_url,isbn,input_date,title,author,publisher,publishing,rating,review,price,ranking,salePrice,point

        coverUrl = browser.find_element(By.CSS_SELECTOR, '.portrait_img_box.portrait img').get_attribute('src')


        # ISBN이 테이블에 존재하는지 확인하는 SQL 쿼리
        check_sql = "SELECT COUNT(*) AS a FROM books WHERE isbn = %s"

        # 새 데이터를 삽입하는 SQL 쿼리
        insert_sql = """INSERT INTO books(isbn, title, author, publisher, publishing, coverUrl)
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



        sql = """INSERT INTO price(
            isbn,inputDate,kyoboPrice,kyoboSalePrice,kyoboPoint
            )
            VALUES(
                %s,%s,%s,%s,%s
            )
            """
        cur.execute(sql, (isbn,inputDate,kyoboPrice,kyoboSalePrice,kyoboPoint))


        sql = """INSERT INTO ranking(
            isbn,inputDate,kyoboRank,kyoboRating,kyoboReview
            )
            VALUES(
                %s,%s,%s,%s,%s
            )
            """
        cur.execute(sql, (isbn,inputDate,kyoboRank,kyoboRating,kyoboReview))




        conn.commit()

        time.sleep(2)

