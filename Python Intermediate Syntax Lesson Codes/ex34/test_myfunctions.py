import unittest
from myfunctions import add, subtract, multiply, divide

# 例子一


class TestMyFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 3), -3)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ValueError, divide, 10, 0)

# if __name__ == '__main__':
#     unittest.main()

# 例子二


class TestMyFunctions(unittest.TestCase):
    def setUp(self):
        # 设置测试环境
        print("setUp")
        self.test_value_a = 10
        self.test_value_b = 5

    def tearDown(self):
        # 清理测试环境
        print("tearDown\n")
        del self.test_value_a
        del self.test_value_b

    def test_add(self):
        self.assertEqual(add(self.test_value_a, self.test_value_b), 15)

    def test_subtract(self):
        self.assertEqual(subtract(self.test_value_a, self.test_value_b), 5)

# 例子三


class TestMyFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 设置测试环境，在所有测试开始前只执行一次
        print("setUpClass")
        cls.shared_value_a = 10
        cls.shared_value_b = 5

    @classmethod
    def tearDownClass(cls):
        # 清理测试环境，在所有测试结束后只执行一次
        print("tearDownClass")
        del cls.shared_value_a
        del cls.shared_value_b

    def test_add(self):
        self.assertEqual(add(self.test_value_a, self.test_value_b), 15)

    def test_subtract(self):
        self.assertEqual(subtract(self.test_value_a, self.test_value_b), 5)
