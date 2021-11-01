class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mult(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            print(Err)

        return x / y

    def sq(self, x):
        return x**2

    def sqrt(self, x):
        return x**(1/2)

    def varexp(self, x, y):
        return x**y

    def inverse(self, x):
        return 1 / x

    def invert_sign(self, x):
        return x * -1



# add lots more methods to this calculator class.
