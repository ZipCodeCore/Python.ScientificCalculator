import unittest
import math
from calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 4), 7)
        self.assertEqual(c.add(-3, -4), -7)
        self.assertTrue(c.add(3, -4), -1)

    def test_eval_function(self):
        c = Calculator()
        self.assertEqual(c.eval_function("qw+2"), "Err")
        self.assertEqual(c.eval_function("1 + 2"), 3)

    def test_subtract(self):
        c = Calculator()
        self.assertEqual(c.subtract(3, 4), -1)
        self.assertEqual(c.subtract(-3, -4), 1)
        self.assertTrue(c.subtract(3, -4), 7)

    def test_multiply(self):
        c = Calculator()
        self.assertEqual(c.multiply(3, 4), 12)
        self.assertEqual(c.multiply(-3, -4), 12)
        self.assertTrue(c.multiply(3, -4), -12)

    def test_divide(self):
        c = Calculator()
        self.assertEqual(c.divide(3, 4), .75)
        self.assertEqual(c.divide(-3, -4), .75)
        self.assertEqual(c.divide(3, -4), -.75)
        self.assertEqual(c.divide(3, 0), "Err")

    def test_square(self):
        c = Calculator()
        self.assertEqual(c.square(3), 9)
        self.assertEqual(c.square(-4), 16)
        self.assertEqual(c.square(0), 0)

    def test_exp(self):
        c = Calculator()
        self.assertEqual(c.exp(3, 4), 81)
        self.assertEqual(c.exp(3, -4), (1 / 3) * (1 / 3) * (1 / 3) * (1 / 3))
        self.assertEqual(c.exp(-3, -4), (-(1 / 3)) * (-(1 / 3)) * (-(1 / 3)) * (-(1 / 3)))
        self.assertEqual(c.exp(0, 0), 1)

    def test_square_root(self):
        c = Calculator()
        self.assertEqual(c.square_root(-2), "Err")
        self.assertEqual(c.square_root(9), 3)
        self.assertEqual(c.square_root(0), 0)
        
 #    def test_invert(self):
 #        c = Calculator()
 #        self.assertEqual(c.invert(2), 0.2)
 # #       self.assertEqual(c.inv(0),"Err")

    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_subtract2(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_multiply2(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_divide2(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_invert(self):
        c = Calculator()
        self.assertEqual(c.invert(5), .2)
        self.assertEqual(c.invert(0), "Err")
        self.assertEqual(c.invert(-5), -.2)

    def test_sin(self):
        c = Calculator()
        c.degrees = False
        half_pi = .5 * math.pi
        self.assertEqual(c.sin(half_pi),1)
        self.assertEqual(c.sin("sdf"),"Err")
        c.degrees = True
        self.assertEqual(c.sin(90), 1)

    def test_cosine(self):
        c = Calculator()
        c.degrees = False
        half_pi = .5 * math.pi
        self.assertAlmostEqual(c.cosine(half_pi),0)
        self.assertEqual(c.cosine("sdf"),"Err")
        c.degrees = True
        self.assertAlmostEqual(c.cosine(90), 0)

    def test_tangent(self):
        c = Calculator()
        c.degrees = False
        quarter_pi = .25 * math.pi
        self.assertAlmostEqual(c.tangent(quarter_pi),1)
        self.assertEqual(c.tangent("sdf"),"Err")
        c.degrees = True
        self.assertAlmostEqual(c.tangent(45), 1)

    def test_invsine(self):
        c = Calculator()
        c.degrees = False
        half_pi = .5 * math.pi
        self.assertEqual(c.inverse_sine(1),half_pi)
        self.assertEqual(c.inverse_sine("sdfsdf"),"Err")
        c.degrees = True
        self.assertEqual(c.inverse_sine(1),90)

    def test_inverse_cosine(self):
        c = Calculator()
        c.degrees = False
        half_pi = .5 * math.pi
        self.assertEqual(c.inverse_cosine(0),half_pi)
        self.assertEqual(c.inverse_cosine("sdfsdf"),"Err")
        c.degrees = True
        self.assertEqual(c.inverse_cosine(0),90)

    def test_inverse_tangent(self):
        c = Calculator()
        c.degrees = False
        quarter_pi = .25 * math.pi
        self.assertEqual(c.inverse_tangent(1),quarter_pi)
        self.assertEqual(c.inverse_tangent("sdfsdf"),"Err")
        c.degrees = True
        self.assertEqual(c.inverse_tangent(1),45)


if __name__ == '__main__':
    unittest.main()
