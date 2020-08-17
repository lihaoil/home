import pytest
import time
from selenium import webdriver


@pytest.fixture()
def user_list_value():
    username = 'selenium'
    loginname = 'selenium_test'
    password = '111111'
    repassword = '111111'
    mail = '2219493104@qq.com'
    phone = '13511074919'
    surper_administrator = '0'


class Test_ODCEMS_System_Userlist():

    def setup(self):
        '''访问测试环境'''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.fullscreen_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://10.220.20.174/#/login')
        self.driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys('admin')
        self.driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys('123456')
        self.driver.find_element_by_xpath("//button[@type='button']").click()

    def teardown(self):
        '''退出浏览器'''
        self.driver.quit()

    def test_odcems_system_userlist_create(self):
        self.driver.find_element_by_partial_link_text("系统管理").click()
        time.sleep(1)
        self.driver.find_element_by_partial_link_text("用户管理").click()
