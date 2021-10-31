import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    """ Whenever this test case is executed,
        setUp() method gets executed first.
        In our case, we simply create an object
        of the Calculator class and save it as a class attribute."""

    def setUp(self):
        self.calculator = Calculator()

    """ write test_xxx methods to test each method in the Calculator class.
        This tells Python (via unittest framework) that these are test methods.
        assertEqual in order to check if the Calculator methods returns 
        the expected value."""

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_sub(self):
        self.assertEqual(self.calculator.sub(10,5), 5)

    def test_mult(self):
        self.assertEqual(self.calculator.mult(3,7), 21)

    def test_div(self):
        self.assertEqual(self.calculator.div(10,2), 5)

""" runs the test case TestCalculator. It execute each test method 
    defined inside the class and gives us the result."""
if __name__ == "__main__":
    unittest.main()
