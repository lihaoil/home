import pytest


# 测试用例按照order的顺序进行执行
@pytest.mark.run(order=2)
def test_add():
    print('test_add')
    assert value == 10

@pytest.mark.run(order=1)
def test_app():
    print('test_app')
    global value
    value = 10
    assert value == 10