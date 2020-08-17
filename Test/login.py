class log():
    def login(dr):
        '''
        登入
        :return:
        '''
        dr.switch_to.frame(dr.find_element_by_xpath('//iframe[@frameborder="0"]'))
        dr.find_element_by_xpath('//input[@name="email"]').clear()
        dr.find_element_by_xpath('//input[@name="email"]').send_keys('13511074919')
        dr.find_element_by_xpath('//input[@name="password"]').clear()
        dr.find_element_by_xpath('//input[@name="password"]').send_keys('wei.1shi.2hao.3')
        dr.find_element_by_xpath('//a[@id="dologin"]').click()

    def logout(dr):
        '登出'
        dr.find_element_by_link_text('退出').click()
        dr.find_element_by_xpath('//a[@id="js-relogin"]').click()