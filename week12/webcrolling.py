import time
from bs4 import  BeautifulSoup
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Options

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get('https://coffeebeankorea.com/store/store.asp')
driver.execute_script("storePop2(385")
time.sleep(5)
html = driver.page_source
soupCB= BeautifulSoup(html, "html.parser")
print(soupCB.prettify())
#driver=webdriver.Chrome(chromedriver.exe)
# driver=webdriver.Chrome()

store_name=h2 = soupCB.select('div.store_txt'>'h2')
print('store_name_h2')
store_name = store_name_h2[0].spring
store_info=soupCB.select('div.store_txt > table.store.txt > td>tag')
store_address_list = list(store_info[2])
print(store_address_list)ddddddddddddddddddddddddd





d