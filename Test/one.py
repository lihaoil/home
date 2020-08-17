class public():
    def login(dr,username,password):
        dr.find_element_by_xpath('//input[@type="text"]').clear()
        dr.find_element_by_xpath('//input[@type="text"]').send_keys(username)
        dr.find_element_by_xpath('//input[@type="password"]').clear()
        dr.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        dr.find_element_by_xpath('//button[@type="button"]').click()
    def logout(dr):
        dr.find_element_by_xpath('//li[@class="header-menu-item"]').click()