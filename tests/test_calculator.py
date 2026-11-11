import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(4, 3), 7)

    def test_addition_with_negative_number(self):
        self.assertEqual(self.calculator.add(-4, 3), -1)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(9, 5), 4)

    def test_subtraction_result_is_negative(self):
        self.assertEqual(self.calculator.subtract(3, 8), -5)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(6, 7), 42)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calculator.multiply(10, 0), 0)

    def test_division(self):
        self.assertEqual(self.calculator.divide(20, 4), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
