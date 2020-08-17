import pytest


# 用于需要重复调用的测试用例
@pytest.fixture()
def test_log():
    print('\n登录')

# @pytest.mark.usefixtures('test_log')使用这个装饰器，测试用例就不用添加test_log这个参数了，使用场景为不想变更之前测试用例的情况下
# @pytest.mark.usefixtures('test_log')
def test_login(test_log):
    print('登录后操作1')

def test_loglog():
    print('不需要登录操作')

# @pytest.mark.usefixtures('test_log')
def test_logout(test_log):
    print('登录后操作2')


# scope='module'意思为fixture生效范围为模块，module整个模块只生效一次
# autouse=True用于自动应用
@pytest.fixture(scope='module', autouse=True)
def test_yield():
    print('测试yield')
    # yield用于执行用例后的后续操作，例如销毁关闭
    yield
    print('销毁yield')
    print('关闭yield')

def test_yield_1(test_yield):
    print('yield生效1')

def test_yiele_2():
    print('yield不生效')

def test_yield_3(test_yield):
    print('yield生效2')



if __name__ == '__main__':
    pytest.main('test_pytest5.py')