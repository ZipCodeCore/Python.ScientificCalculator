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

    def test_sin_deg(self):
        self.assertEqual(self.calculator.sin_deg(45), 0.7071067811865475)

    def test_sin_rad(self):
        self.assertEqual(self.calculator.sin_rad(45), 0.8509035245341184)

    def test_cos_deg(self):
        self.assertEqual(self.calculator.cos_deg(45), 0.7071067811865476)

    def test_cos_rad(self):
        self.assertEqual(self.calculator.cos_rad(45), 0.5253219888177297)

    def test_tan_deg(self):
        self.assertEqual(self.calculator.tan_deg(45), 0.9999999999999999)

    def test_tan_rad(self):
        self.assertEqual(self.calculator.tan_rad(45), 1.6197751905438615)

    def test_inv_sin_deg(self):
        self.assertEqual(self.calculator.inv_sin_deg(45), 0.7071067811865475)

    def test_inv_sin_rad(self):
        self.assertEqual(self.calculator.inv_sin_rad(45), 0.8509035245341184)

    def test_inv_cos_deg(self):
        self.assertEqual(self.calculator.inv_cos_deg(45), 0.7071067811865476)

    def test_inv_cos_rad(self):
        self.assertEqual(self.calculator.inv_cos_rad(45), 0.5253219888177297)

    def test_inv_tan_deg(self):
        self.assertEqual(self.calculator.inv_tan_deg(45), 0.9999999999999999)

    def test_inv_tan_rad(self):
        self.assertEqual(self.calculator.inv_tan_rad(45), 1.6197751905438615)

    def test_trig_units_mode_deg_to_rad(self):
        self.assertEqual(self.calculator.trig_units_mode_deg_to_rad(45), 0.7853981633974483)

    def test_trig_units_mode_rad_to_deg(self):
        self.assertEqual(self.calculator.trig_units_mode_rad_to_deg(45), 2578.3100780887044)

    def test_factorial(self):
        self.assertEqual(self.calculator.factorial(5), 120)

    def test_log(self):
        self.assertEqual(self.calculator.log(45, 10), 1.6532125137753435)

    def test_inverse_log(self):
        self.assertEqual(self.calculator.inverse_log(3), 1000)

    def test_inv_ln(self):
        self.assertEqual(self.calculator.inv_ln(3), 20.085536923187668)

    def test_pi(self):
        self.assertEqual(self.calculator.pi(), 3.141592653589793)

    def test_e(self):
        self.assertEqual(self.calculator.e(), 2.718281828459045)


""" runs the test case TestCalculator. executes each test method 
    defined in the class and gives us the result."""
if __name__ == "__main__":
    unittest.main()
