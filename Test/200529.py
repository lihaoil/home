from selenium import webdriver
from one import public
from time import sleep

class log():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://10.220.20.205/#/login')

    def user_admin(self):
        username = 'admin'
        password = 'Admin321'
        public().login(self.driver,username,password)
        sleep(3)
        self.driver.quit()

    def user_wei(self):
        username = 'wei'
        password = 'Admin321'
        public().login(self.driver,username,password)
        sleep(3)
        self.driver.quit()

log().user_admin()
log().user_wei()