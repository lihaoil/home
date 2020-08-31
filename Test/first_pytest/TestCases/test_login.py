import pytest
import allure
from selenium import webdriver


username_password = [{'username': 'admin', 'password': 123456},
                     {'username': 'wsh', 'password': 111111},
                     {'username': 'hsw', 'password': 111111}]

@pytest.fixture(scope='module')
def test_parameter(request):
    username = request.param['username']
    password = request.param['password']
    return username, password

@allure.testcase('登录测试')
class Test_Login():
    
driver = webdriver.Edge()

    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://10.220.20.174/#/login')

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

    @pytest.mark.parametrize('test_parameter', username_password, indirect=True)
    def test_login1(self, test_parameter):
        print(test_parameter)
        self.driver.find_element_by_xpath('//input[@type="text"]').send_keys(test_parameter[0])
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(test_parameter[1])
        self.driver.find_element_by_xpath('//button[@type="button"]').click()