import unittest
from calculator import Calculator



def runTest(self, prompt_str, expected_out):
    with patch('builtins.input', return_value=prompt_str), patch('sys.stdout', new=StringIO()) as fake_out:
        answer()
        self.assertEqual(enter_num(), expected_out)


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 4), 7)
        self.assertEqual(c.add(-3,-4), -7)
        self.assertTrue(c.add(3,-4), -1)

    def test_subtract(self):
        c = Calculator()
        self.assertEqual(c.subtract(3, 4), -1)
        self.assertEqual(c.subtract(-3,-4), 1)
        self.assertTrue(c.subtract(3,-4), 7)

    def test_multiply(self):
        c = Calculator()
        self.assertEqual(c.multiply(3, 4), 12)
        self.assertEqual(c.multiply(-3,-4), 12)
        self.assertTrue(c.multiply(3,-4), -12)
    def test_divide(self):
        c = Calculator()
        self.assertEqual(c.divide(3, 4), .75)
        self.assertEqual(c.divide(-3,-4), .75)
        self.assertEqual(c.divide(3,-4), -.75)
        self.assertEqual(c.divide(3,0),"Err")
    def test_square(self):
        c = Calculator()
        self.assertEqual(c.square(3), 9)
        self.assertEqual(c.square(-4), 16)
        self.assertEqual(c.square(0), 0)
    def test_exp(self):
        c = Calculator()
        self.assertEqual(c.exp(3, 4), 81)
        self.assertEqual(c.exp(3, -4), (1/3)*(1/3)*(1/3)*(1/3))
        self.assertEqual(c.exp(-3, -4), (-(1/3))*(-(1/3))*(-(1/3))*(-(1/3)))
        self.assertEqual(c.exp(0, 0), 1)
    def test_square_root(self):
        c = Calculator()
        self.assertEqual(c.square_root(-2), "Err")
        self.assertEqual(c.square_root(9), 3)
        self.assertEqual(c.square_root(0),0)

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

    def test_inv(self):
        c = Calculator()
        self.assertEqual(c.inv(5), .2)
        self.assertEqual(c.inv(0), "Err")
        self.assertEqual(c.inv(-5), -.2)

    def test_sine(self):
        pass

    def test_cosine(self):
        pass

    def test_tangent(self):
        pass

    def test_invsine(self):
        pass




if __name__ == '__main__':
    unittest.main()
