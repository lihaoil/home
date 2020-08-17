import pytest
import time
from selenium import webdriver


@pytest.fixture()
def username_password_value():
    username = 'admin'
    password = '123456'
    return (username,password)


class Test_ODCEMS():

    def setup(self):
        '''访问测试环境'''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.fullscreen_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://10.220.20.174/#/login')

    def teardown(self):
        '''退出浏览器'''
        self.driver.quit()

    def test_odcems_login(self,username_password_value):
        '''输入用户名密码登录'''
        self.driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys(username_password_value[0])
        self.driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys(username_password_value[1])
        self.driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(1)
        url = self.driver.current_url
        pytest.assume(url == 'http://10.220.20.174/#/index/staffAttendance')
        print(self.driver.title)
        print(self.driver.current_url)