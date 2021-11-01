import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """ When the test case is executed,
        setUp() method gets executed first."""

    def setUp(self):
        self.calculator = Calculator()

    """ test each method in the Calculator class.
        assertEqual checks if the Calculator methods returns 
        the expected value."""

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_sub(self):
        self.assertEqual(self.calculator.sub(10, 5), 5)

    def test_mult(self):
        self.assertEqual(self.calculator.mult(3, 7), 21)

    def test_div(self):
        self.assertEqual(self.calculator.div(10, 2), 5)

    def test_sq(self):
        self.assertEqual(self.calculator.sq(2), 4)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_varexp(self):
        self.assertEqual(self.calculator.varexp(10, 2), 100)

    def test_inverse(self):
        self.assertEqual(self.calculator.inverse(10), 0.1)

    def test_invert_sign(self):
        self.assertEqual(self.calculator.invert_sign(10), -10)
