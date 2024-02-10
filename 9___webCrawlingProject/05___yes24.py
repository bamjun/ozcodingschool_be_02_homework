from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import pymysql, pass1, time, re


ChromeDriverManager().install()

browser = webdriver.Chrome()


link_list = []
for x in range(1, 2):
    print("*"*10, f'현재 {x} 페이지 수집 중 입니다.', '*'*10)
    url = f'https://www.yes24.com/Product/Category/DayBestSeller?categoryNumber=001&pageNumber={x}&pageSize=100&type=day&saleDts='
    browser.get(url)
    time.sleep(1)

    datas = browser.find_elements(By.CLASS_NAME, 'gd_name')
    for i in datas:
        link = i.get_attribute('href')
        link_list.append(link)
    time.sleep(3)



# 데이터 베이스 연동 후 -> 수집한 데이터를 DB에 저장 (csv)
conn = pymysql.connect(
    host='localhost',
    user='root',
    password= pass1.password(),
    db = 'booksminiproject',
    cursorclass = pymysql.cursors.DictCursor
)

with conn.cursor() as cur:
    for x in range(len(link_list)):
        link = link_list[x]
        max_attempts = 2
        attempts = 0

        while attempts < max_attempts:
            try:
                browser.get(link)

                title = browser.find_element(By.CLASS_NAME, 'gd_name').text
                author = browser.find_element(By.CLASS_NAME, 'gd_auth').text


                isbn13_xpath = "//tr[th[text()='ISBN13']]/td"
                isbn13_element = browser.find_element(By.XPATH, isbn13_xpath)
                isbn = isbn13_element.text

                inputDate = datetime.now().strftime('%Y-%m-%d')

                coverUrl = browser.find_element(By.CLASS_NAME, 'gImg').get_attribute('src')


                publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text

                publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text
                
                match = re.search(r'(\d+)년 (\d+)월 (\d+)일', publishing)


                if match:
                    year, month, day = match.groups()
                    data_obj = datetime(int(year), int(month), int(day))
                    publishing = data_obj.strftime("%Y-%m-%d")
                else:
                    publishing = "0000-00-00"


                    
                price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
                yes24Price = int(price.replace(',', ''))

                
                price = browser.find_element(By.CLASS_NAME, 'nor_price').text[:-1]
                yes24SalePrice = int(price.replace(',', ''))


                price = browser.find_element(By.CSS_SELECTOR, '.gd_infoLi li').text
                match = re.search(r"([\d,]+)원", price)
                yes24Point = int(match.group(1).replace(',', ''))


                yes24Rank = x + 1


                yes24Rating = browser.find_elements(By.CSS_SELECTOR, '.gd_rating a em.yes_b')
                if len(yes24Rating) > 0:
                    yes24Rating = yes24Rating[0].text
                else:
                    yes24Rating = 0


                yes24Review = browser.find_elements(By.CSS_SELECTOR, '.gd_reviewCount em.txC_blue')
                if len(yes24Review) > 0:
                    yes24Review = yes24Review[0].text.replace(',', '')
                else:
                    yes24Review = 0


                time.sleep(2)

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



        sql = """INSERT INTO yes24_price(
            isbn,inputDate,yes24Price,yes24SalePrice,yes24Point, yes24url
            )
            VALUES(
                %s,%s,%s,%s,%s,%s
            )
            """
        cur.execute(sql, (isbn,inputDate,yes24Price,yes24SalePrice,yes24Point, link))


        sql = """INSERT INTO yes24_ranking(
            isbn,inputDate,yes24Rank,yes24Rating,yes24Review
            )
            VALUES(
                %s,%s,%s,%s,%s
            )
            """
        cur.execute(sql, (isbn,inputDate,yes24Rank,yes24Rating,yes24Review))



        conn.commit()

        time.sleep(2)



conn.close()


