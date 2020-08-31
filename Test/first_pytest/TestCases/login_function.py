import time
from selenium import webdriver
from first_pytest.util.find_element import FindElement


class LoginFunction(object):

    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    # 获取driver,打开url
    def get_driver(self, url, i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(2)
        return driver

    # 获取定位语句
    def get_element(self, section, key):
        get_element = FindElement(self.driver)
        element = get_element.find_element(section, key)
        return element

    # 定位元素，输入信息
    def send_info(self, section, key, data):
        self.get_element(section, key).send_keys(data)

    # 定位元素，单击
    def click_button(self, section, key):
        self.get_element(section, key).click()

    # 定位元素，获取文本
    def get_text(self, section, key):
        text = self.get_element(section, key).text
        return text

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()
        self.driver.quit()