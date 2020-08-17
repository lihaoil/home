import pytest


test_dict_1 = [{'username':'wei','password':111111},
               {'username':'shi','password':222222},
               {'username':'hao','password':333333},
               {'username':'hao','password':''}]


test_dict_2 = [{'ID':'qwer','count':10,'page':1},
               {'ID':'asdf','count':20,'page':2},
               {'ID':'zxcv','count':30,'page':3}]


@pytest.fixture(scope='module')
def test_login(request):
    ue = request.param['username']
    pd = request.param['password']
    if pd:
        return True
    else:
        return False


@pytest.fixture(scope='module')
def test_logout(request):
    id = request.param['ID']
    count = request.param['count']
    page = request.param['page']
    return id,count,page


@pytest.mark.parametrize('test_logout', test_dict_2,indirect=True)
@pytest.mark.parametrize('test_login', test_dict_1, indirect=True)
def test_login_logout(test_login,test_logout):
    assert test_login, '请输入密码'
    print(test_login)
    print(test_logout)