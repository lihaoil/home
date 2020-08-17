import pytest
import allure
import time
from selenium import webdriver


@allure.testcase('百度搜索功能')
@pytest.mark.parametrize('test_data',['pytest','unittest','allure'])
def test_steps_demo(test_data):
    with allure.step('step one:打开浏览器访问百度'):
        dr = webdriver.Chrome()
        dr.maximize_window()
        dr.get('https://www.baidu.com/')
    with allure.step('step two:输入查询信息'):
        dr.find_element_by_xpath('//input[@id="kw"]').send_keys(test_data)
        time.sleep(2)
        dr.find_element_by_xpath('//input[@id="su"]').click()
        time.sleep(2)
    with allure.step('step three:保存截图'):
        #
        dr.save_screenshot('./result/a.png')
        allure.attach.file('./result/a.png',attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body>首页</body>',attachment_type=allure.attachment_type.HTML)
    with allure.step('step four:关闭浏览器'):
        dr.quit()