import unittest
from tdd.operations_math import addition_math


class TestMath(unittest.TestCase):
    def test_addition(self):
        math_result = addition_math(num_1=5, num_2=5)
        self.assertEqual(math_result, 10)


if __name__ == '__main__':
    unittest.main()
