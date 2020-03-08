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
        if num2 != 0:
            print('Division = ', (num1 / num2))
        else:
            print("Err")
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


cal = Calculator()
print("Scientific calculator")
print("List of choice:")
print('-' * 20)
print("1 : Addition \t\t  12 : Sine in degrees")
print("2 : Subtraction \t  13 : Cosine in degrees")
print("3 : Multiplication \t  14 : Tan in degrees")
print("4 : Division \t\t  15 : Cosecant in degrees")
print("5 : Sine in radians \t  16: Secant in degrees")
print("6 : Cosine in radians \t  17 : cot in degrees")
print("7 : Tan in radians \t  18 : Natural log")
print("8 : Cosecant in radians   19 : Base 10 log")
print("9 : Secant in radians \t  20 : Log base'x'")
print("10 : Cot in radians \t  21 : Square root")
print("11 : pi \t\t  22 : Power of")
print('-' * 20)
choice = ""
while True:
    try:
        choice = int(input("Enter the number of choice: "))
    except:
        print("Enter a valid number: (")
    if choice == 1:
        n1 = float(input("Enter the first number to add : "))
        n2 = float(input("Enter the second number to add : "))
        cal.add(n1, n2)
    elif choice == 2:
        n1 = float(input("Enter the first number to subtract : "))
        n2 = float(input("Enter the second number to subtract : "))
        cal.sub(n1, n2)
    elif choice == 3:
        n1 = float(input("Enter the first number to multiply : "))
        n2 = float(input("Enter the second number to multiply : "))
        cal.mul(n1, n2)
    elif choice == 4:
        n1 = float(input("Enter the first number for division : "))
        n2 = float(input("Enter the second number for division : "))
        cal.div(n1, n2)
    elif choice == 5:
        n = float(input("Enter a number to find its Sine in radians : "))
        cal.sinrad(n)
    elif choice == 6:
        n = float(input("Enter a number to find its Cos in radians : "))
        cal.cosrad(n)
    elif choice == 7:
        n = float(input("Enter a number to find its Tan in radians : "))
        cal.tanrad(n)
    elif choice == 8:
        n = float(input("Enter a number to find its Cosecant in radians : "))
        cal.cosecrad(n)
    elif choice == 9:
        n = float(input("Enter a number to find its Secant in radians : "))
        cal.secrad(n)
    elif choice == 10:
        n = float(input("Enter a number to find its Cot in radians : "))
        cal.cotrad(n)
    elif choice == 11:
        cal.pie()
    elif choice == 12:
        n = float(input("Enter a number to find its Sine in degrees : "))
        cal.sindeg(n)
    elif choice == 13:
        n = float(input("Enter a number to find its Cosine in degrees : "))
        cal.cosdeg(n)
    elif choice == 14:
        n = float(input("Enter a number to find its Tan in degrees : "))
        cal.tandeg(n)
    elif choice == 15:
        n = float(input("Enter a number to find its Cosecant in degrees : "))
        cal.cosecdeg(n)
    elif choice == 16:
        n = float(input("Enter a number to find its Secant in degrees : "))
        cal.secdeg(n)
    elif choice == 17:
        n = float(input("Enter a number to find its Cot in degrees : "))
        cal.cotdeg(n)
    elif choice == 18:
        n = float(input("Enter a number to find its Natural in log : "))
        cal.ln(n)
    elif choice == 19:
        n = float(input("Enter a number to find its Base 10 log : "))
        cal.logten(n)
    elif choice == 20:
        n1 = float(input("Enter base value : "))
        n2 = float(input("Enter a number to find its log to the given log value : "))
        cal.logbasex(n1, n2) # steps are made like functions
    elif choice == 21:
        n = float(input("Enter a number to get it's Square root : "))
        cal.squareroot(n)
    elif choice == 22:
        n1 = float(input("Enter a number : "))
        n2 = float(input("Enter its power"))
        cal.powerof(n1, n2)
    else:
        print("ERROR : Please enter a valid number ")
