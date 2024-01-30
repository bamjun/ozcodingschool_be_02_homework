from selenium import webdriver
import requests, time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()
user = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

url = "https://kream.co.kr/"
driver.get(url)


driver.find_element(BY)

btn_search
