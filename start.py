from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Ie()
url = 'https://google.com'
driver.get(url)
# driver.maximize_window()  # 화면 최대화
action = ActionChains(driver)


driver.find_element_by_css_selector('#gb_70').click()  # 우측 상단 로그인 버튼 클릭
time.sleep(2)

action.send_keys('kwangsoo.yoo@gmail.com').perform()  # email 주소 입력
driver.find_element_by_css_selector('.CwaK9').click()  # 다음 버튼 클릭
time.sleep(2)
