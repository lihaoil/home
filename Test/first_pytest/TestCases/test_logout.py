import time
from selenium import webdriver


driver = webdriver.Edge()

#登录
def driver_init():
    driver.get('https://www.baidu.com/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(2)

#获取元素
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#操作元素
def get_click(id):
    driver.find_element_by_id(id).click()

def run_main():
    driver_init()
    get_element('kw').send_keys('测试')
    get_click('su')

run_main()