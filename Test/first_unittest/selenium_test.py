import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://bbs.51testing.com/member.php?mod=regurl')

driver.find_element_by_class_name('pnpnc').click()


driver.close()
driver.quit()