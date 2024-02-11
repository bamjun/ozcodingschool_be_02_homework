
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, re
from datetime import datetime
from selenium import webdriver

chrome_driver_path = '/path/to/chromedriver'
chrome_options = webdriver.ChromeOptions()
# Chrome 실행 파일의 경로를 지정해야 할 경우, 아래 옵션을 사용
# chrome_options.binary_location = '/path/to/google-chrome'

ChromeDriverManager().install()
browser = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

link_list = []
for x in range(1, 6):
    print("*"*10, f'현재 {x} 페이지 수집 중 입니다.', '*'*10)
    url = f'https://product.kyobobook.co.kr/bestseller/online?period=001&dsplDvsnCode=001&dsplTrgtDvsnCode=002&saleCmdtDsplDvsnCode=TOT&page={x}'
    
    browser.get(url)

    datas = browser.find_elements(By.CLASS_NAME, 'auto_overflow_inner a.prod_info')
    datas = datas
    for i in datas:
        link = i.get_attribute('href')
        link_list.append(link)
    time.sleep(3)





for x in range(len(link_list)):
    link = link_list[x]
    max_attempts = 2
    attempts = 0

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

            kyoboRank = x + 1

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


    


    print(isbn, title, author, publisher, publishing, coverUrl)



