import math

class Basic_func(object):

    def __init__(self):
        self.options = {"1": "add"}

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
         return x * y

    def div(self, x, y):
        return x / y

    # def square(self, x):
    #     return x * x
    #
    # def square_rt(self, x):
    #     return math.sqrt(x)
    #
    # def inverse(self,x):
    #     if x == 0:
    #         return "ERR"
    #     else:
    #         return 1 / x
    #
    # def invert_sign(self, x):
    #     return (-1) * x
    #
    #
    # def cal_sin(self, x, unit):
    #     if unit == 2:
    #         return math.asin(x)
    #     elif unit == 1:
    #      return math.sin(x)
    #
    # def cal_cosin(self, x, unit):
    #     if unit == 2:
    #         print("RAdian Value")
    #         return math.acos(x)
    #     elif unit == 1:
    #         print("Degree Value")
    #         return math.cos(x)
    #
    # def cal_tang(self, x, unit):
    #     if unit == 2:
    #         return math.atan(x)
    #     elif unit == 1:
    #         return math.tan(x)
    #
    # def inverse_sin(self, x, unit):
    #     val = self.cal_sin(x, unit)
    #     return 1/val
    #
    # def inverse_cosin(self, x, unit):
    #     val = self.cal_cosin(x, unit)
    #     return 1/val
    #
    # def inverse_tang(self,x, unit):
    #     val = self.cal_tang(x, unit)
    #     return 1/val




# add lots more methods to this calculator class.
