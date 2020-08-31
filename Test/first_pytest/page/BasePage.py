import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException, TimeoutException, NoAlertPresentException, NoSuchFrameException
from selenium import webdriver

class BasePage(object):
    '''

    '''

    def __init__(self):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'tag_name': By.TAG_NAME,
            'link_text': By.LINK_TEXT,
            'class_name': By.CLASS_NAME,
            'css_selector': By.CSS_SELECTOR,
            'partial_link_text': By.PARTIAL_LINK_TEXT
        }