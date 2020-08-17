import pytest


# 跳过某些测试用例
@pytest.mark.skip
def test_skip():
    print('跳过不执行')


# phone = 'android'
phone = 'apple'
# 满足某些条件后才能执行。否则跳过
# @pytest.mark.skipif("phone=='android'", reason='安卓没有此功能')
@pytest.mark.skipif(phone=='android', reason='安卓没有此功能')
def test_phone():
    print('安卓不执行')


# 不执行
@pytest.mark.xfail
def test_xfail():
    print(er())

def er():
    raise Exception('报错')