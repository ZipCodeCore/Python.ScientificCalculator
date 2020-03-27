import unittest
from calculator import Calculator


class TestStringMethods(unittest.TestCase):
c = Calculator()

    def test_add(self):
        self.assertEqual(c.add(3, 3), 6)
        self.assertEqual(c.add(12, -10), 2)
        self.assertEqual(c.add(5, 8), 13)

    def test_sub(self):
        self.assertEqual(c.sub(9, 3), 6)
        self.assertEqual(c.sub(-4, 3), -7)
        self.assertEqual(c.sub(123.2, .2), 123)

    def test_mul(self):
        self.assertEqual(c.mul(4, .5), 2)
        self.assertEqual(c.mul(5, 5), 25)
        self.assertEqual(c.mul(10, -1), -10)

    def test_div(self):
        self.assertEqual(c.div( 25,5 ), 5)
        self.assertEqual(c.div( 10,-2 ),-5)
        self.assertEqual(c.div( 10,-2 ),-5)
        self.assertEqual(c.div( 10,-2 ),-5)

    def test_powerof(self):
        c = Calculator()
        self.assertEqual(c.powerof(10, 5), 100000)
        self.assertEqual(c.powerof(10, -2), .01)

    def test_square(self):
        self.assertEqual(c.square(10), 100)
        self.assertEqual(c.square(-10), 100)
        self.assertEqual(c.square(0), 0)

    def test_squarert(self):
        c = Calculator()
        self.assertEqual(c.squareroot(25), 5)
        self.assertEqual(c.squareroot(100), 10)

    def test_sinrad(self):
        c = Calculator()
        self.assertEqual(c.sinrad(3), 0.14112001)
        self.assertEqual(c.sinrad(2), -0.90929743)

    def test_cosrad(self):
        self.assertEqual(c.cosrad(90), -0.44807362)
        self.assertEqual(c.cosrad(-2), -0.41614684)

    def test_tanrad(self):
        self.assertEqual(c.tanrad(50), -0.27190061)
        self.assertEqual(c.tanrad(-124), -10.73213753)

    def test_secrad(self):
        self.assertEqual(c.secrad(68), 2.27198876)
        self.assertEqual(c.secrad(-90), -2.23177613)

    def test_cosecrad(self):
        self.assertEqual(c.secrad(-90), -1.11857241)
        self.assertEqual(c.secrad(65), 1.20944039)

    def test_cotrad(self):
        self.assertEqual(c.secrad(-50), 3.67781445)
        self.assertEqual(c.secrad(90), -.50120278)

    def test_sindeg(self):
        self.assertEqual(c.sindeg(3), 0.05233596)
        self.assertEqual(c.sindeg(90), 1)

    def test_cosdeg(self):
        self.assertEqual(c.cosdeg(90), 0)
        self.assertEqual(c.cosdeg(38), .78801075)

    def test_tandeg(self):
        self.assertEqual(c.tandeg(50), 1.19175359)
        self.assertEqual(c.tandeg(-124), 1.48256097)

    def test_secdeg(self):
        self.assertEqual(c.secdeg(68), 2.66946716)
        self.assertEqual(c.secdeg(-9), 1.01246513)

    def test_cosecdeg(self):
        self.assertEqual(c.secdeg(-9), -6.39245322)
        self.assertEqual(c.secdeg(65), 1.10337792)

    def test_cotdeg(self):
        self.assertEqual(c.secdeg(65), .46630766)
        self.assertEqual(c.secdeg(-65), -.46630766)

    def test_factorial(self):
        self.assertEqual(c.factorial(10), 3628800)

    def test_ln(self):
        self.assertEqual(c.ln(65), 4.1743872699)

    def test_logten(self):
        self.assertEqual(c.logten(45), 1.65321251378)

    def test_logbasex(self):
        self.assertEqual(c.logbasex(60, 20), 1.3667257913)
        
if __name__ == '__main__':
    unittest.main()
