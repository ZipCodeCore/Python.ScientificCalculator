import math


class Calculator:

    def __init__(self):
        pass

    def add(self, num1, num2):
        answer = num1 + num2
        return answer

    def sub(self, num1, num2):
        answer = num1 - num2
        return answer

    def mul(self, num1, num2):
        answer = num1 * num2
        return answer

    def div(self, num1, num2):
        if num2 != 0:
            answer = (num1 / num2)
            return answer
       
    def powerof(self, num, raiseby):
        answer = math.pow(num, raiseby)
        return answer

    def square(self, num):
        answer = math.pow(num, 2)
        return answer

    def squareroot(self, num):
        answer = math.sqrt(num)
        return answer

    def inverse(self, num):
        answer = 1/(num)
        return answer

    def switchsign(self, num):
        answer = num*(-1)
        return answer

    def sinrad(self, num):
        answer = math.sin(num)
        return answer

    def cosrad(self, num):
        answer = math.cos(num)
        return answer

    def tanrad(self, num):
        answer = math.tan(num)
        return answer

    def cosecrad(self, num):
        answer = 1/(math.sin(num))
        return answer

    def secrad(self, num):
        answer = 1/(math.cos(num))
        return answer

    def cotrad(self, num):
        answer = 1/(math.tan(num))
        return answer

    def sindeg(self, num):
        answer = math.sin(math.radians(num))
        return answer

    def cosdeg(self, num):
        answer = math.cos(math.radians(num))
        return answer

    def tandeg(self, num):
        answer = math.tan(math.radians(num))
        return answer

    def cosecdeg(self, num):
        answer = 1/(math.sin(math.radians(num)))
        return answer

    def secdeg(self, num):
        answer = 1/(math.cos(math.radians(num)))
        return answer

    def cotdeg(self, num):
        answer = 1/(math.tan(math.radians(num)))
        return answer

    def factorial(self, num):
        answer = math.factorial(num)
        return answer

    def ln(self, num):
        answer = math.log(num)
        return answer

    def logten(self, num):
        answer = math.log10(num)
        return answer

    def logbasex(self, num, x):
        answer = math.log(num, x)
        return answer