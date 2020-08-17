import pytest


def setup_module():
    print('模块级别开始')

def teardown_module():
    print('模块级别结束')

def setup_function():
    print('函数级别开始')

def teardown_function():
    print('函数级别结束')

def test_2():
    print('222')


class TestSet():

    def setup_class(self):
        print('类级别开始')

    def teardown_class(self):
        print('类级别结束')

    def setup_method(self):
        print('方法级别开始')

    def teardown_method(self):
        print('方法级别结束')

    def test_1(self):
        print('111')


if __name__ == '__main__':
    pytest.main('-s','test_pytest4.py')