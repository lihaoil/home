import configparser


class ReadIni(object):

    def __init__(self, in_file=None):
        if in_file == None:
            in_file = 'D:/Project/Test/first_pytest/config/config.ini'
        self.config = self.load_ini(in_file)

    # 加载config.ini配置文件
    def load_ini(self, in_file):
        config = configparser.ConfigParser()
        config.read(in_file)
        return config

    # 获取定位元素信息
    def get_value(self, section, key):
        location = self.config.get(section, key)
        return location