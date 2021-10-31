import math

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


    # added by KB

    def switchDisplayMode(self,string_mode,x):
        """
        Switch display mode (binary, octal, decimal, hexadecimal)
        switchDisplayMode(String mode) should set the display to the mode given
        :param string_mode:
        :return:
        """
        #binary=0
        #counter=0
        #temp=x
        if (string_mode == 'bin'):
            # while (temp > 0):
            # base = 2
            # binary = ((temp % base))
            # print(binary)
            return str(bin(int(x)).replace("0b", ""))  # STATE TO BE MODIFIED AS NEEDED
        elif (string_mode == 'dec'):
            return str(round(float(x), 2))
        elif (string_mode == 'oct'):
            return str(oct(int(x)).replace("0o", ""))
        elif (string_mode == 'hex'):
            return str(hex(int(x)).replace("0x", ""))
        else:
            return str('invalid selection')

    def sin_deg(self, x):
        x=math.radians(x)
        return math.sin(x)

    def sin_rad(self, x):
        return math.sin(x)

    def cos_deg(self, x):
        return math.cos(math.radians(x))

    def cos_rad(self, x):
        return math.cos(x)

    def tan_deg(self, x):
        return math.tan(math.radians(x))

    def tan_rad(self, x):
        return math.tan(x)

    def inv_sin_deg(self, x):
        return math.sin(math.radians(x))

    def inv_sin_rad(self, x):
        return math.sin(x)

    def inv_cos_deg(self, x):
        return math.cos(math.radians(x))

    def inv_cos_rad(self, x):
        return math.cos(x)

    def inv_tan_deg(self, x):
        return math.tan(math.radians(x))

    def inv_tan_rad(self, x):
        return math.tan(x)

    def trig_units_mode_deg_to_rad(self, x):
        return math.radians(x)

    def trig_units_mode_rad_to_deg(self, x):
        return math.degrees(x)

    def factorial(self,x ):
        return math.factorial(self.state)

    def log(self, x, base):
        return math.log(x,base)

    def inverse_log(self,x):
        return 10**x

    def ln(self, x):
        return math.ln(x)

    def inv_ln(self,x):
        return math.exp(x)

    #def logTen(self, self.state):
        #return math.log10(self.state)

    def pi(self):
        return math.pi

    def e(self):
        return math.e