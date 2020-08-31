from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://10.220.20.174/#/login')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//input[@type="text"]').send_keys('admin')
driver.find_element_by_xpath('//input[@type="password"]').send_keys('123456')
driver.find_element_by_xpath('//button[@type="button"]').click()

driver.find_element_by_xpath('//*[@id="menu-a"]/ul/li[6]/div[1]').click()
driver.find_element_by_xpath('//*[@id="menu-a"]/ul/li[6]/div[2]').click()
driver.find_element_by_xpath('//*[@id="menu-a"]/ul/li[6]/div[2]/ul/li[1]/a').click()

driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/button[2]').click()
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/form/div[1]/div/div[1]/input').send_keys('1')
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/form/div[2]/div/div[1]/input').send_keys('111')
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/form/div[3]/div/div[1]/input').send_keys('111111')
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/form/div[4]/div/div[1]/input').send_keys('111111')

text = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/form/div[1]/div/div[2]').text
print(text)

# driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/div/button[1]/span').click()
# driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div/div/div[3]/button[2]/span').click()
time.sleep(10)
driver.close()
driver.quit()