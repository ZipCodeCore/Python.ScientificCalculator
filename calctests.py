import unittest
from calculator import Calculator


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

    def test_sub2(self):
        c = Calculator()
        self.assertEqual(c.sub(-4, 3), -7)

   def test_sub3(self):
        c = Calculator()
        self.assertEqual(c.sub(123.2, .2), 123)
    
   def test_mul1(self):
        c = Calculator()
        self.assertEqual(c.mul(4, .5), 2)

    def test_mul2(self):
        c = Calculator()
        self.assertEqual(c.mul(5, 5), 25)
    
    def test_mul3(self):
        c = Calculator()
        self.assertEqual(c.mul(10, -1), -10)
   
    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div( 25,5 ), 5)

    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div( 10,-2 ),-5)
    
    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div( 10,-2 ),-5)
 
    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div( 10,-2 ),-5)

if __name__ == '__main__':
    unittest.main()
