import pytest
from selenium import webdriver


@pytest.fixture()
class Test_Cloud_Class_Browser():
    def test_cloud_def_browser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://10.220.20.205/#/login')
        yield
        driver.quit()
