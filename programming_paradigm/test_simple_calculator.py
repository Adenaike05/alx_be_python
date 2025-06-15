import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
      
        self.calc = SimpleCalculator()
        print(f"\nSetting up calculator for test: {self._testMethodName}") # Optional: to see test execution flow

    def tearDown(self):
       
        self.calc = None 
        print(f"Tearing down calculator after test: {self._testMethodName}") # Optional

    
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -2), 3)
        self.assertEqual(self.calc.add(-7, 3), -4)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(-5, 0), -5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_float_numbers(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(self.calc.add(-1.5, 1.5), 0.0)

    # --- Test methods for 'subtract' ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3) # -5 - (-2) = -5 + 2 = -3
        self.assertEqual(self.calc.subtract(-2, -5), 3)  # -2 - (-5) = -2 + 5 = 3

    def test_subtract_positive_from_negative(self):
        self.assertEqual(self.calc.subtract(-10, 5), -15)

    def test_subtract_with_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract_float_numbers(self):
        self.assertAlmostEqual(self.calc.subtract(7.5, 2.5), 5.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2)
        self.assertAlmostEqual(self.calc.subtract(10.0, 10.0), 0.0)

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(5, -4), -20)
        self.assertEqual(self.calc.multiply(-6, 3), -18)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiply_float_numbers(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 0.5), 0.75)

    # --- Test methods for 'divide' ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_positive_by_negative(self):
        self.assertEqual(self.calc.divide(10, -2), -5.0)

    def test_divide_negative_by_positive(self):
        self.assertEqual(self.calc.divide(-10, 2), -5.0)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Also test 0/0

    def test_divide_zero_by_non_zero(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), -0.0) # Python handles -0.0

    def test_divide_float_numbers(self):
        self.assertAlmostEqual(self.calc.divide(7.0, 2.0), 3.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

if __name__ == '__main__':
    unittest.main(verbosity=2) # verbosity=2 shows more detailed test results