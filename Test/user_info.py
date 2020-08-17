from selenium import webdriver
from time import sleep
from one import public

user_flie = open('user_info.txt','r')
lines = user_flie.readlines()
user_flie.close()

for line in lines:
    username = line.split(',')[0]
    password = line.split(',')[1]
    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.implicitly_wait(10)
    dr.get('http://10.220.20.205/#/login')
    public.login(dr,username,password)
    print(111)
    sleep(3)
    dr.quit()