import math


class intermediate:


    def square(self,x):
        result = x ** 2
        print ("Square = ", result)


    def squareroot(self,x):
        result = math.sqrt(x)
        print ("Squareroot = ", result)


    def exponential(self,x, y):
        result = x ** y
        print ("Exponential = ", result)


    def sine(self,x):
        result = math.sin()
        print ("sin = ", result)


    def cosine(self,x):
        result = math.cos()
        print ("cos = ", result)


    def tang(self,x):
        result = math.tan()
        print ("tan = ", result)


    def asine(self,x):
        result = math.asin()
        print ("inverse sin = ", result)


    def acosine(self,x):
        result = math.acos()
        print ("inverse cos = ", result)


    def atang(self,x):
        result = math.atan()
        print ("inverse tan = ", result)


answer = intermediate()
answer.square(5)