# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, with test method names
    adjusted to precisely match the external checker's requirements.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method runs.
        """
        self.calc = SimpleCalculator()
        # print(f"\nSetting up calculator for test: {self._testMethodName}") # Optional: for verbose output

    def tearDown(self):
        """
        Clean up after each test method runs.
        """
        self.calc = None
        # print(f"Tearing down calculator after test: {self._testMethodName}") # Optional

    # --- Test method for 'add' (already passing) ---
    def test_addition(self):
        """Test the add method with various types of numbers and scenarios."""
        # Positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 200), 300)
        # Negative numbers
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-10, -5), -15)
        # Positive and negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -2), 3)
        self.assertEqual(self.calc.add(-7, 3), -4)
        # With zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(-5, 0), -5)
        self.assertEqual(self.calc.add(0, 0), 0)
        # Floating-point numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(self.calc.add(-1.5, 1.5), 0.0)

    # --- Test method for 'subtract' (already passing) ---
    def test_subtraction(self):
        """Test the subtract method with various types of numbers and scenarios."""
        # Positive numbers
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        # Negative numbers
        self.assertEqual(self.calc.subtract(-5, -2), -3) # -5 - (-2) = -5 + 2 = -3
        self.assertEqual(self.calc.subtract(-2, -5), 3)  # -2 - (-5) = -2 + 5 = 3
        # Positive and negative numbers
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15) # 10 - (-5) = 10 + 5 = 15
        # With zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Floating-point numbers
        self.assertAlmostEqual(self.calc.subtract(7.5, 2.5), 5.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2)
        self.assertAlmostEqual(self.calc.subtract(10.0, 10.0), 0.0)

    # --- Test method for 'multiply' (RENAMED from test_multiply) ---
    def test_multiplication(self): # Renamed from test_multiply
        """Test the multiply method with various types of numbers and scenarios."""
        # Positive numbers
        self.assertEqual(self.calc.multiply(2, 4), 8)
        self.assertEqual(self.calc.multiply(10, 10), 100)
        # Negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Positive and negative numbers
        self.assertEqual(self.calc.multiply(5, -4), -20)
        self.assertEqual(self.calc.multiply(-6, 3), -18)
        # With zero
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        # Floating-point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 0.5), 0.75)

    # --- Test method for 'divide' (RENAMED from test_divide) ---
    def test_division(self): # Renamed from test_divide
        """Test the divide method with various types of numbers and edge cases."""
        # Normal positive division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        # Division with negative numbers
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        # Division by zero (edge case)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # 0 divided by 0 also results in None as per method logic
        # Zero divided by non-zero
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), -0.0)
        # Floating-point division
        self.assertAlmostEqual(self.calc.divide(7.0, 2.0), 3.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

if __name__ == '__main__':
    unittest.main(verbosity=2)