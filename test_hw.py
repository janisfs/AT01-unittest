import unittest
from main_hw import calculate_remainder


# Тест на вычисление остатка от деления
class TestCalculateRemainder(unittest.TestCase):
    def test_non_zero_divisor(self):
        self.assertEqual(calculate_remainder(10, 3), 1)
        self.assertEqual(calculate_remainder(7, 2), 1)

    # Тест на деление на ноль
    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            calculate_remainder(10, 0)


if __name__ == '__main__':
    unittest.main()