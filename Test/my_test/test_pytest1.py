import time
import pytest
import allure

def add(x,y):
    return x+y

@allure.severity(allure.severity_level.BLOCKER)
def test_add():
    print('test one')
    assert add(1,2) == 3

@allure.severity(allure.severity_level.CRITICAL)
def test_add2():
    print('test two')
    assert add(2,3) == 5
    time.sleep(5)
    assert add(5,6) == 11

@allure.severity(allure.severity_level.NORMAL)
def test_add3():
    print('test three')
    assert add(1,9) == 10

@allure.severity(allure.severity_level.MINOR)
def test_add4():
    print('test four')
    # pytest.assume中间断言失败，代码仍继续执行
    pytest.assume(1 + 4 == 5)
    pytest.assume(1 + 3 == 4)
    pytest.assume(2 + 5 == 7)
    pytest.assume(2 + 5 == 7)
    print("测试完成")