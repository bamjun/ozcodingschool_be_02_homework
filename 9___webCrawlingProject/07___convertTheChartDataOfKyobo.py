import pymysql, pass1, time, re
from datetime import datetime


conn = pymysql.connect(
    host='localhost',
    user='root',
    password= pass1.password(),
    db = 'booksminiproject',
    cursorclass = pymysql.cursors.DictCursor
)

with conn.cursor() as cur:
    data = {"datasets": []}
    for rank, x in enumerate(lst_all, 1):
        a = x.select_one(".up")
        if a:
            title = x.select_one(".ellipsis.rank01").text.strip()
            singer = x.select_one(".ellipsis.rank02").text.strip()
            elbum = x.select_one(".ellipsis.rank03").text.strip()
            data["datasets"].append(
                {
                    "label": f"{singer} - {title}🔼{a.text}",
                    "data": [
                        {"x": rank, "y": int(a.text), "r": 10},
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



conn.close()








