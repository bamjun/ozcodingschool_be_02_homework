from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


options = Options()
# 창안띄우고 크롤링
# options.add_argument("--headLess")

user = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

url = "https://kream.co.kr/"
driver.get(url)


driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
time.sleep(0.5)

classText = ".input_search.show_placeholder_on_focus"
driver.find_element(By.CSS_SELECTOR, classText).send_keys("슈프림")
time.sleep(0.3)

driver.find_element(By.CSS_SELECTOR, classText).send_keys(Keys.ENTER)
time.sleep(0.1)
screen_path = "C:/Projects/oz_coding/ozcodingschool_be_02_homework/7___oz_crawling/kream_screenshot/ab"
for i in range(5):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(0.1)
    driver.save_screenshot(screen_path + str(i) + ".png")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# items = soup.select(".item_inner")
items = soup.select(".search_result_item.product")

for num, i in enumerate(items):
    product_name = i.select_one(".translated_name")
    if "후드" in product_name.text:  # 슈프림 후드 사커 저지 브라이트 그린
        # 너버 1부터
        # num
        # 브랜드명
        brand_name = i.select_one(".product_info_brand.brand").text
        # 제품명
        product_name = product_name.text
        # 가격
        price = i.select_one(".amount").text
        # 리뷰수
        review = i.select_one(".review_figure").text
        # 즐찾수
        wish = i.select_one(".wish_figure").text
        string = f"🔽\nNo : {num}\n브랜드 : {brand_name}\n"
        string += f"제품명 : {product_name}\n가격 : {price}\n"
        string += f"리뷰수 : {review}\n즐겨찾기수 : {wish}\n\n"
        print(string)

# driver.quit()
