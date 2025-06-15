import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):    
        self.calc = SimpleCalculator()

    def tearDown(self):
        self.calc = None
    def test_addition(self):
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


    # --- Test methods for 'subtract' ---
    # This method is specifically named 'test_subtraction' as implied by the checks.
    def test_subtraction(self):
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

    # --- Test methods for 'multiply' ---
    # This method is specifically named 'test_multiply' as implied by the checks.
    def test_multiply(self):
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

    # --- Test methods for 'divide' ---
    # This method is specifically named 'test_divide' as implied by the checks.
    def test_divide(self):
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
        self.assertEqual(self.calc.divide(0, -5), -0.0) # Python's representation of negative zero
        # Floating-point division
        self.assertAlmostEqual(self.calc.divide(7.0, 2.0), 3.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

if __name__ == '__main__':
    unittest.main(verbosity=2)