import unittest
from main_3 import divide

class TestMath(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)


if __name__ == '__main__':
    unittest.main()

