import math

class Calculator:

    def __init__(self):
        error = False
        value = 0

    def err(self):
        self.error = True


    def add(self, a, b):
        print(self, a + b)
        return a + b


    def subtract(self, x, y):
        print(self, x - y)
        return x - y


    def multiply(self, x, y):
        print(self, x * y)
        return y * x


    def divide(self, x, y):
        try:
            result = x / y
        except:
            result = "Err"
            self.err()

        return result


    def square(self, base):
        print(self, base ** 2)
        return base ** 2


    def exp(self, x, y):
        print(self, x ** y)
        return x ** y


    def square_root(self, x):
        try:
            print(math.sqrt(x))
        except:
            self.err()
            return "Err"
        return math.sqrt(x)


    def inv(self, x):
        try:
            result = 1/x
        except:
            self.err()
            return "Err"
        print(1 / x)
        return 1 / x


##SECONDARY FORMULAS

    def add2(self, x):
        print(self, returned_result + x)
        return returned_result + x


    def subtract2(self, x):
        print(self, returned_result - x)
        return returned_result - x


    def multiply2(self, x):
        print(self, returned_result * x)
        return returned_result * x


    def divide2(self, x):
        print(self, returned_result / x)
        return returned_result / x