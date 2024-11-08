import unittest
from main_2 import check


# Тест на четность
class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertTrue(not check(1))
        self.assertTrue(not check(3))
        self.assertTrue(not check(57))

        self.assertFalse(check(5))
        self.assertFalse(check(7))
        self.assertFalse(check(11))



if __name__ == '__main__':
    unittest.main()



