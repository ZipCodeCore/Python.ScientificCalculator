import unittest
from .calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 3), 6)

    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(12, -10), 2)

    def test_add3(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_sub(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 3), 6)

    def test_mul(self):
        c = Calculator()
        self.assertEqual(c.mul(6, 8), 48)


    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div(10, 2), 5)


    def test_inverse(self):
        c = Calculator()
        self.assertEqual(c.inverse(10), 0.1)


    def test_invert_sign(self):
        c = Calculator()
        self.assertEqual(c.invert_sign(10), -10)


    def test_square(self):
        c = Calculator()
        self.assertEqual(c.square(10), 100)


    def test_square_rt(self):
        c = Calculator()
        self.assertEqual(c.square_rt(4), 2)











if __name__ == '__main__':
    unittest.main()
