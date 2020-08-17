from selenium import webdriver
from login import log
from time import sleep
from one import public

dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(10)
#dr.get("https://mail.163.com/")
dr.get('https://www.baidu.com')

dr.find_element_by_css_selector('[name="wd"][class="s_ipt"]').send_keys('admin')
sleep(3)
dr.find_element_by_xpath('//input[@id="su').click()
print(dr.title)