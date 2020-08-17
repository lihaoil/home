import pytest


test_list = [1,2,3,'wei']


test_dict = [{'name':'wei','age':18},
             {'name':'shi','age':19},
             {'name':'hao','age':20}]


@pytest.fixture()
def test_parameter(request):
    print('数据准备')
    name = request.param['name']
    age = request.param['age']
    return name,age


# 参数化驱动，indirect=True表示将test_parameter当成函数去执行，参数为test_dict
@pytest.mark.parametrize('test_parameter', test_dict, indirect=True)
def test_parameter_example(test_parameter):
    print('准备的数据为：{}'.format(test_parameter))


if __name__ == '__main__':
    pytest.main('-s','test_pytest7.py')