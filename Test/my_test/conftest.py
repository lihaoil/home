# conftest.py文件时当前文件夹路径下数据共享文件，公共模块放到这里
import pytest


@pytest.fixture()
def test_conftest():
    print('公共文件')