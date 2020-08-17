import unittest

class second_test(unittest.TestCase):

    # 执行每个class开始都需要执行的
    @classmethod
    def setUpClass(cls) -> None:
        print('begin')
        cls.foo = list(range(5))
        print(cls.foo)

    # 执行每个class结束都需要执行的
    @classmethod
    def tearDownClass(cls) -> None:
        print('end')

    def test_1(self):
        print('test_1')
        self.assertEqual(self.foo.pop(),4)
        print(self.foo)

    def test_2(self):
        print('test_2')
        self.assertEqual(self.foo.pop(),3)
        print(self.foo)


if __name__ == '__main__':
    unittest.main()