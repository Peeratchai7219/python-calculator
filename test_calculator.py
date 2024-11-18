import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add_positive(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-3, -5), -8)
        
    # Test cases for subtract()
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-5, -10), 5)

     # Test cases for multiply()
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    # Test cases for divide()
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(12, 3), 4)
    
    # Test cases for divide()
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(12, 3), 4)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-12, 3), -4)

    

if __name__ == '__main__':
    unittest.main()