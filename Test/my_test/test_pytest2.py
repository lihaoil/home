import pytest
import random


# 参数化
@pytest.mark.parametrize('x,y',[
    ('1+1',2),
    ('a','b'),
    ('1+2',3),
    ('c','c'),
])
def test_xy(x,y):
    # eval将str字符串当成有效的表达式计算后返回结果
    assert eval(x) == y


data = [1,2,3,4,5]


@pytest.mark.parametrize('x', data)
def test_x(x):
    assert x == random.randint(1,3)