
import math

class Calculator:

    def __init__(self):

        self.error = False
        self.result = 0
        self.degrees = True
        self.display_mode = "decimal"
        self.stored_number = 0

    def err(self):
        self.error = True

    def eval_function(self, x: str) -> float:
        """
        evaluates x to return a result
        """
        return eval(x)



    def add(self, a, b):
        """
        ADDS TWO NUMBERS AND RETURNS RESULT
        :param a:
        :param b:
        :return:
        """
        print( a + b)
        return a + b


    def subtract(self, x, y):
        """
        SUBTRACTS TWO NUMBERS AND RETURNS RESULT
        :param x:
        :param y:
        :return:
        """
        print( x - y)
        return x - y


    def multiply(self, x, y):
        """
        MULTIPLIES TWO NUMBERS AND RETURNS RESULT
        :param x:
        :param y:
        :return:
        """
        print( x * y)
        return y * x


    def divide(self, x, y):

        """
        DIVIDES TWO NUMBERS AND RETURNS RESULT
        :param x:
        :param y:
        :return:
        """
        try:
            result = x / y
        except:
            result = "Err"
            self.err()

        return result


    def square(self, base):
        """
        SQUARES A NUMBER AND RETURNS RESULT
        :param base:
        :return:
        """
        print( base ** 2)
        return base ** 2


    def exp(self, x, y):
        """
        EXPONENTIATES TWO NUMBERS AND RETURNS RESULT
        :param x:
        :param y:
        :return:
        """
        print( x ** y)
        return x ** y


    def square_root(self, x):
        """
        FINDS THE SQUARE ROOT OF A NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        try:
            print(math.sqrt(x))
        except:
            self.err()
            return "Err"
        return math.sqrt(x)


    def inv(self, x):
        """
        INVERSES A NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        try:
            result = 1/x
        except:
            self.err()
            return "Err"
        print(1 / x)
        """
        FINDS THE SQUARE ROOT OF A NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        print( x ** (1 / 2))
        return x ** (1 / 2)


    def inverse(self, x):
        """
        INVERSES A NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        print( 1 / x)
        return 1 / x

    def deg_rad_swap(self):
        """
        SWAPS BETWEEN RADIANS AND DEGREES
        :return:
        """
        self.degrees = not self.degrees

    def sin(self, x):
        """
        FINDS SINE OF NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        if self.degrees:
            x = math.radians(x)
        return math.sin(x)

    def cosine(self, x):
        """
        FINDS COSINE OF NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        if self.degrees:
            x = math.radians(x)
        return math.cos(x)

    def tangent(self, x):
        """
        FINDS TANGENT OF NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        if self.degrees:
            x = math.radians(x)
        return math.tan(x)

    def inverse_sine(self, x):
        """
        FINDS INVERSE SINE OF NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        if self.degrees:
            x = math.radians(x)
        return math.asin(x)

    def inverse_cosine(self, x):
        """
        FINDS INVERSE COSINE OF NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        if self.degrees:
            x = math.radians(x)
        return math.acos(x)

    def inverse_tangent(self, x):
        """
        FINDS INVERSE TANGENT OF NUMBER AND RETURNS RESULT
        :param x:
        :return:
        """
        if self.degrees:
            x = math.radians(x)
        return math.atan(x)

    ##SECONDARY FORMULAS

    def add2(self, x):
        """
        ADDS A NUMBER WITH THE SAME NUMBER
        :param x:
        :return:
        """
        print(self.result + x)
        return self.result + x


    def subtract2(self, x):
        """
        SUBTRACTS A NUMBER WITH THE SAME NUMBER
        :param x:
        :return:
        """
        print(self.result - x)
        return self.result - x


    def multiply2(self, x):
        """
        MULTIPLIES A NUMBER WITH THE SAME NUMBER
        :param x:
        :return:
        """
        print( self.result * x)
        return self.result * x


    def divide2(self, x):
        """
        DIVIDES A NUMBER WITH THE SAME NUMBER
        :param x:
        :return:
        """

        print( returned_result / x)
        return returned_result / x

        print( self.result / x)
        return self.result / x


