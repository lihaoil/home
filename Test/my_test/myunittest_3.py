import unittest

# 执行每个模块开始都需要执行的
def setUpModule():
    print('begin')
    global foo
    foo = list(range(1,20))

# 执行每个模块结束都需要执行的
def tearDownModule():
    print('end')


class third_test(unittest.TestCase):

    def test_1(self):
        print('test_1')
        self.assertEqual(foo.pop(), 17)
        print(foo)

    def test_2(self):
        print('test_2')
        self.assertEqual(foo.pop(), 16)
        print(foo)


class fourth_test(unittest.TestCase):

    def test_3(self):
        print('test_3')
        self.assertEqual(foo.pop(), 19)
        print(foo)

    def test_4(self):
        print('test_4')
        self.assertEqual(foo.pop(), 18)
        print(foo)