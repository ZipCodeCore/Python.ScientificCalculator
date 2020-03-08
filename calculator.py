import math


class Calculator(object):
    def add(self, num1, num2):
        answer = num1 + num2
        print('Sum = ', answer)
    def sub(self, num1, num2):
        answer = num1 - num2
        print('Difference = ', answer)
    def mul(self, num1, num2):
        answer = num1 * num2
        print('Multiplication = ', answer)
    def div(self, num1, num2):
        answer = num1 / num2
        print('Division = ', answer)
    def powerof(self, num, raiseby):
        answer = math.pow(num, raiseby)
        print('%f ^ %f = %f' % (num, raiseby, answer))
    def square(self, num):
        answer = math.pow(num, 2)
    def squareroot(self, num):
        answer = math.sqrt(num)
        print("Square root (%f) = %f" % (num, answer))
    def inverse(self, num):
        answer = 1/(num)
        print('Inverse (%f) = %f' % (num, answer))
    def switchsign(self, num):
        print(1-(num<=0))
    def sinrad(self, num):
        answer = math.sin(num)
        print('Sine (%f) = %f' %(num, answer))
    def cosrad(self, num):
        answer = math.cos(num)
        print('Cosine (%f) = %f' %(num, answer))
    def tanrad(self, num):
        answer = math.tan(num)
        print('Tangent (%f) = %f' %(num, answer))
    def cosecrad(self, num):
        answer = 1/(math.sin(num))
        print('Inverse Sine(%f) = %f' % (num, answer))
    def secrad(self, num):
        answer = 1/(math.cos(num))
        print('Inverse Cosine(%f) = %f' % (num, answer))
    def cotrad(self, num):
        answer = 1/(math.tan(num))
        print('Inverse Tangent(%f) = %f' % (num, answer))
    def sindeg(self, num):
        answer = math.sin(math.radians(num))
        print('Sin(%f) in Degrees = %f' % (num, answer))
    def cosdeg(self, num):
        answer = math.cos(math.radians(num))
        print('Cos(%f) in Degrees = %f' % (num, answer))
    def tandeg(self, num):
        answer = math.tan(math.radians(num))
        print('Tan(%f) in Degrees = %f' % (num, answer))
    def cosecdeg(self, num):
        answer = 1/(math.sin(math.radians(num)))
        print('Inverse Sine(%f) in Degrees = %f' % (num, answer))
    def secdeg(self, num):
        answer = 1/(math.cos(math.radians(num)))
        print('Inverse Cosine(%f) in degrees = %f' % (num, answer))
    def cotdeg(self, num):
        answer = 1/(math.tan(math.radians(num)))
        print('Inverse Tangent(%f) in degrees = %f' % (num, answer))
    def factorial(self, num):
        answer = math.factorial(num)
        print('Factorial (%f) = %f' % (num, answer))
    def ln(self, num):
        answer = math.log(num)
        print('Log (%f) = %f' % (num, answer))
    def logten(self, num):
        answer = math.log10(num)
        print('Log10(%f) = %f' % (num, answer))
    def logbasex(self, num, x):
        answer = math.log(num, x)
        print('Log base (%f)(%f) = %f' % (x, num, answer))
    def pie(self):
        print('pi = ', math.pi)
    def e_constant(self):
        print('e = ', math.e)

