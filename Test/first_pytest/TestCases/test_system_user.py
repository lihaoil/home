import time
from first_pytest.TestCases.login_function import LoginFunction


def test_system_user():

    screenshot = 'D:/Project/Test/first_pytest/report/test_error_001.png'
    # 登录
    test = LoginFunction('http://10.220.20.174/#/login', 1)
    test.send_info('LoginElement', 'username', 'admin')
    test.send_info('LoginElement', 'password', '123456')
    test.click_button('LoginElement', 'button')
    # 跳转到用户管理菜单
    test.click_button('UserManagementElement', 'menu1')
    test.click_button('UserManagementElement', 'menu2')
    test.click_button('UserManagementElement', 'menu3')
    # 创建用户
    test.click_button('UserManagementElement', 'create')
    test.send_info('UserManagementElement', 'username', '111')
    test.send_info('UserManagementElement', 'login_name', '111')
    test.send_info('UserManagementElement', 'password', '111111')
    test.send_info('UserManagementElement', 'confirm_password', '111111')
    # 创建失败截图处理
    username_error = test.get_element('UserManagementElement', 'username_error')
    if username_error == None:
        print('创建成功')
    else:
        test.driver.get_screenshot_as_file(screenshot)
    # 确定创建
    test.click_button('UserManagementElement', 'confirm')
    test.click_button('UserManagementElement', 'reconfirm')
    # 关闭
    time.sleep(5)
    test.close_browser()

test_system_user()