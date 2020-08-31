from first_pytest.util.read_ini import ReadIni


class FindElement(object):

    def __init__(self, driver):
        self.driver = driver

    # 获取定位信息
    def find_element(self, section, key):
        ini = ReadIni()
        location = ini.get_value(section, key)
        by = location.split('->')[0]
        value = location.split('->')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'tag_name':
                return self.driver.find_element_by_tag_name(value)
            elif by == 'class_name':
                return self.driver.find_element_by_class_name(value)
            elif by == 'link_text':
                return self.driver.find_element_by_link_text(value)
            elif by == 'partial_link_text':
                return self.driver.find_element_by_partial_link_text(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'css_selector':
                return self.driver.find_element_by_css_selector(value)
        except:
            return None