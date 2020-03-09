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

    def test_div1(self):
        c = Calculator()
        self.assertEqual(c.div( 25,5 ), 5)

    def test_div2(self):
        c = Calculator()
        self.assertEqual(c.div( 10,-2 ),-5)

    def test_div3(self):
        c = Calculator()
        self.assertEqual(c.div( 10,-2 ),-5)

    def test_div4(self):
        c = Calculator()
        self.assertEqual(c.div( 10,-2 ),-5)

    def test_powerof1(self):
        c = Calculator()
        self.assertEqual(c.powerof(10, 5), 100000)

    def test_powerof2(self):
        c = Calculator()
        self.assertEqual(c.powerof(10, -2), .01)

    def test_square1(self):
        c = Calculator()
        self.assertEqual(c.square(10), 100)


    def test_square2(self):
        c = Calculator()
        self.assertEqual(c.square(-10), 100)

    def test_square3(self):
        c = Calculator()
        self.assertEqual(c.square(0), 0)

    def test_squarert(self):
        c = Calculator()
        self.assertEqual(c.squareroot(25), 5)

    def test_squarert2(self):
        c = Calculator()
        self.assertEqual(c.squareroot(100), 10)

    def test_sinrad1(self):
        c = Calculator()
        self.assertEqual(c.sinrad(3), 0.14112001)

    def test_sinrad2(self):
        c = Calculator()
        self.assertEqual(c.sinrad(2), -0.90929743)

    def test_cosrad1(self):
        c = Calculator()
        self.assertEqual(c.cosrad(90), -0.44807362)

    def test_cosrad2(self):
        c = Calculator()
        self.assertEqual(c.cosrad(-2), -0.41614684)

    def test_tanrad1(self):
        c = Calculator()
        self.assertEqual(c.tanrad(50), -0.27190061)

    def test_tanrad2(self):
        c = Calculator()
        self.assertEqual(c.tanrad(-124), -10.73213753)

    def test_secrad1(self):
        c = Calculator()
        self.assertEqual(c.secrad(68), 2.27198876)

    def test_secrad2(self):
        c = Calculator()
        self.assertEqual(c.secrad(-90), -2.23177613)

    def test_cosecrad1(self):
        c = Calculator()
        self.assertEqual(c.secrad(-90), -1.11857241)

    def test_cosecrad2(self):
        c = Calculator()
        self.assertEqual(c.secrad(65), 1.20944039)

    def test_cotrad1(self):
        c = Calculator()
        self.assertEqual(c.secrad(-50), 3.67781445)

    def test_cotrad2(self):
        c = Calculator()
        self.assertEqual(c.secrad(90), -.50120278)

    def test_sindeg1(self):
        c = Calculator()
        self.assertEqual(c.sindeg(3), 0.05233596)

    def test_sindeg2(self):
        c = Calculator()
        self.assertEqual(c.sindeg(90), 1)

    def test_cosdeg1(self):
        c = Calculator()
        self.assertEqual(c.cosdeg(90), 0)

    def test_cosdeg2(self):
        c = Calculator()
        self.assertEqual(c.cosdeg(38), .78801075)

    def test_tandeg1(self):
        c = Calculator()
        self.assertEqual(c.tandeg(50), 1.19175359)

    def test_tandeg2(self):
        c = Calculator()
        self.assertEqual(c.tandeg(-124), 1.48256097)

    def test_secdeg1(self):
        c = Calculator()
        self.assertEqual(c.secdeg(68), 2.66946716)

    def test_secdeg2(self):
        c = Calculator()
        self.assertEqual(c.secdeg(-9), 1.01246513)

    def test_cosecdeg1(self):
        c = Calculator()
        self.assertEqual(c.secdeg(-9), -6.39245322)

    def test_cosecdeg2(self):
        c = Calculator()
        self.assertEqual(c.secdeg(65), 1.10337792)

    def test_cotdeg1(self):
        c = Calculator()
        self.assertEqual(c.secdeg(65), .46630766)

    def test_cotdeg2(self):
        c = Calculator()
        self.assertEqual(c.secdeg(-65), -.46630766)

    def test_factorial(self):
        c = Calculator()
        self.assertEqual(c.factorial(10), 3628800)

    def test_ln(self):
        c = Calculator()
        self.assertEqual(c.ln(65), 4.1743872699)

    def test_logten(self):
        c = Calculator()
        self.assertEqual(c.logten(45), 1.65321251378)

    def test_logbasex(self):
        c = Calculator()
        self.assertEqual(c.logbasex(60, 20), 1.3667257913)
if __name__ == '__main__':
    unittest.main()
