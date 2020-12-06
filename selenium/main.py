
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser open
path = "C:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)
url = "http://www.naver.com"
driver.get(url)
time.sleep(2)

# search
 
query_text = "키워드"
element = driver.find_element_by_id("query")
element.send_keys(query_text)
element.send_keys(Keys.RETURN)

 
#d 아이디, 패스워드 로그인 창으로 이동하는 버튼 클릭
