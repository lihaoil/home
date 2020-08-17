import unittest
from HTMLTestRunner import HTMLTestRunner
import os

class first_test(unittest.TestCase):

    # 执行每个test方法开始都需要执行的
    def setUp(self):
        print('begin')
        self.foo = list(range(10))
        print(self.foo)

    # 执行每个test方法结束都需要执行的
    def tearDown(self):
        print('end')

    def test_1(self):
        print('test_1')
        # self.assertEqual(self.foo.pop(),9)

    # unittest.skip用于跳过某些用例不执行
    @unittest.skip
    def test_2(self):
        print('test_2')
        # self.assertEqual(self.foo.pop(),9)

    def test_3(self):
        print('test_3')
        assert 1 == 1
        assert {'name':'wei', 'age':18} == {'name':'wei', 'age':18}
        a = 'hello'
        age = 10
        assert 1 < age < 20
        self.assertIn(a,'hello world')
        self.assertGreater(11, 2, '1不可能比2大')
        self.assertIn('l', 'hello', 'hello包含l')


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    # 当前文件路径
    current_path = os.getcwd()
    # 拼接路径与文件名称
    report_path = os.path.join(current_path,'unittest_report.html')
    # 构造测试套件
    tao = unittest.TestSuite()
    # 添加测试
    tao.addTest(first_test('test_1'))
    tao.addTest(first_test('test_2'))
    tao.addTest(first_test('test_3'))
    fp = open(report_path,'w')
    # 执行测试
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试用例')
    runner.run(tao)
    fp.close()