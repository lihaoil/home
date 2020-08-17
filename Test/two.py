from selenium import webdriver

search_text = [1937,'selenium','中文']

for text in search_text:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys(text)
    driver.find_element_by_id('su').click()
    print(driver.title)
    driver.quit()