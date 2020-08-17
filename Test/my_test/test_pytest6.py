import pytest


list = [1,2,3,'qwer']

@pytest.fixture(params = list)
def test_data(request):
    result = request.param
    return result

def test_data_one(test_data):
    print('test_data is {}'.format(test_data))