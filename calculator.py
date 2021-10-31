import math

class Calculator:

    def __init__(self):
        self.degrees = True


    def add(self, a, b):
        print( a + b)
        return a + b


    def subtract(self, x, y):
        print( x - y)
        return x - y


    def multiply(self, x, y):
        print( x * y)
        return y * x


    def divide(self, x, y):
        print( x / y)
        return x / y


    def square(self, base):
        print( base ** 2)
        return base ** 2


    def exp(self, x, y):
        print( x ** y)
        return x ** y


    def square_root(self, x):
        print( x ** (1 / 2))
        return x ** (1 / 2)


    def inv(self, x):
        print( 1 / x)
        return 1 / x

    def deg_rad_swap(self):
        self.degrees = not self.degrees

    def sin(self, x):
        if self.degrees:
            x = math.radians(x)
        return math.sin(x)

    def cosine(self, x):
        if self.degrees:
            x = math.radians(x)
        return math.cos(x)

    def tangent(self, x):
        if self.degrees:
            x = math.radians(x)
        return math.tan(x)

    def inverse_sine(self, x):
        if self.degrees:
            x = math.radians(x)
        return math.asin(x)

    def inverse_cosine(self, x):
        if self.degrees:
            x = math.radians(x)
        return math.acos(x)

    def inverse_tangent(self, x):
        if self.degrees:
            x = math.radians(x)
        return math.atan(x)

    ##SECONDARY FORMULAS

    def add2(self, x):
        print( returned_result + x)
        return returned_result + x


    def subtract2(self, x):
        print( returned_result - x)
        return returned_result - x


    def multiply2(self, x):
        print( returned_result * x)
        return returned_result * x


    def divide2(self, x):
        print( returned_result / x)
        return returned_result / x