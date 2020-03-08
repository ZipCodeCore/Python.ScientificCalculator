import math


class Calculator(object):
    def add(self, num1, num2):
        answer = num1 + num2
        print('Sum = ', answer)
        return answer
    def sub(self, num1, num2):
        answer = num1 - num2
        print('Difference = ', answer)
        return answer
    def mul(self, num1, num2):
        answer = num1 * num2
        print('Multiplication = ', answer)
        return answer
    def div(self, num1, num2):
        if num2 != 0:
            print('Division = ', (num1 / num2))
            return (num1/num2)
        else:
            print("Err")
    def powerof(self, num, raiseby):
        answer = math.pow(num, raiseby)
        print('%f ^ %f = %f' % (num, raiseby, answer))
        return answer
    def square(self, num):
        answer = math.pow(num, 2)
        print(answer)
        return answer
    def squareroot(self, num):
        answer = math.sqrt(num)
        print("Square root (%f) = %f" % (num, answer))
        return answer
    def inverse(self, num):
        answer = 1/(num)
        print('Inverse (%f) = %f' % (num, answer))
        return answer
    def switchsign(self, num):
        print(1-(num<=0))
        return answer
    def sinrad(self, num):
        answer = math.sin(num)
        print('Sine (%f) = %f' %(num, answer))
        return answer
    def cosrad(self, num):
        answer = math.cos(num)
        print('Cosine (%f) = %f' %(num, answer))
        return answer
    def tanrad(self, num):
        answer = math.tan(num)
        print('Tangent (%f) = %f' %(num, answer))
        return answer
    def cosecrad(self, num):
        answer = 1/(math.sin(num))
        print('Inverse Sine(%f) = %f' % (num, answer))
        return answer
    def secrad(self, num):
        answer = 1/(math.cos(num))
        print('Inverse Cosine(%f) = %f' % (num, answer))
        return answer
    def cotrad(self, num):
        answer = 1/(math.tan(num))
        print('Inverse Tangent(%f) = %f' % (num, answer))
        return answer
    def sindeg(self, num):
        answer = math.sin(math.radians(num))
        print('Sin(%f) in Degrees = %f' % (num, answer))
        return answer
    def cosdeg(self, num):
        answer = math.cos(math.radians(num))
        print('Cos(%f) in Degrees = %f' % (num, answer))
        return answer
    def tandeg(self, num):
        answer = math.tan(math.radians(num))
        print('Tan(%f) in Degrees = %f' % (num, answer))
        return answer
    def cosecdeg(self, num):
        answer = 1/(math.sin(math.radians(num)))
        print('Inverse Sine(%f) in Degrees = %f' % (num, answer))
        return answer
    def secdeg(self, num):
        answer = 1/(math.cos(math.radians(num)))
        print('Inverse Cosine(%f) in degrees = %f' % (num, answer))
        return answer
    def cotdeg(self, num):
        answer = 1/(math.tan(math.radians(num)))
        print('Inverse Tangent(%f) in degrees = %f' % (num, answer))
        return answer
    def factorial(self, num):
        answer = math.factorial(num)
        print('Factorial (%f) = %f' % (num, answer))
        return answer
    def ln(self, num):
        answer = math.log(num)
        print('Log (%f) = %f' % (num, answer))
        return answer
    def logten(self, num):
        answer = math.log10(num)
        print('Log10(%f) = %f' % (num, answer))
        return answer
    def logbasex(self, num, x):
        answer = math.log(num, x)
        print('Log base (%f)(%f) = %f' % (x, num, answer))
        return answer
    def pie(self):
        print('pi = ', math.pi)
        return answer
    def e_constant(self):
        print('e = ', math.e)
        return answer


cal = Calculator()


def contin(y):
    cal = Calculator()
    cont = int(input("If you would like to stop type 1\nIf you would like to contine type 2\n"))
    if cont == 1:
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
    elif cont == 2:
        fun = int(input("1 : Addition \t\t 2 : Subtraction\n3 : Multiplication \t 4 : Division\n5 : Square root \t 6 : Squared\n"))
        contined(fun,y)
    else:
        print("Sorry try again")
        contin(y)

def contined(picked,y):
    if picked == 1:
        num2 = int(input("What number would you like to add?\n"))
        z = cal.add(int(y),int(num2))
        contin(z)
    if picked == 2:
        num2 = int(input("What number would you like to subtract?\n"))
        z = cal.sub(int(y),int(num2))
        contin(z)
    if picked == 3:
        num2 = int(input("What number would you like to multiply by?\n"))
        z = cal.mul(int(y), int(num2))
        contin(z)
    if picked == 4:
        num2 = int(input("What number would you like to divide by?\n"))
        z = cal.div(int(y), int(num2))
        contin(z)
    if picked == 5:
        z = cal.squareroot(int(y))
        contin(z)
    if picked == 6:
        z = cal.square(int(y))
        contin(z)





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
    except ValueError:
        print("Enter a valid number: ")
    if choice == 1:
        n1 = float(input("Enter the first number to add : "))
        n2 = float(input("Enter the second number to add : "))
        x = cal.add(n1, n2)
        contin(x)
    elif choice == 2:
        n1 = float(input("Enter the first number to subtract : "))
        n2 = float(input("Enter the second number to subtract : "))
        x = cal.sub(n1, n2)
        contin(x)
    elif choice == 3:
        n1 = float(input("Enter the first number to multiply : "))
        n2 = float(input("Enter the second number to multiply : "))
        x = cal.mul(n1, n2)
        contin(x)
    elif choice == 4:
        n1 = float(input("Enter the first number for division : "))
        n2 = float(input("Enter the second number for division : "))
        x = cal.div(n1, n2)
        contin(x)
    elif choice == 5:
        n = float(input("Enter a number to find its Sine in radians : "))
        x = cal.sinrad(n)
        contin(x)
    elif choice == 6:
        n = float(input("Enter a number to find its Cos in radians : "))
        x = cal.cosrad(n)
        contin(x)
    elif choice == 7:
        n = float(input("Enter a number to find its Tan in radians : "))
        x = cal.tanrad(n)
        contin(x)
    elif choice == 8:
        n = float(input("Enter a number to find its Cosecant in radians : "))
        x = cal.cosecrad(n)
        contin(x)
    elif choice == 9:
        n = float(input("Enter a number to find its Secant in radians : "))
        x = cal.secrad(n)
        contin(x)
    elif choice == 10:
        n = float(input("Enter a number to find its Cot in radians : "))
        x = cal.cotrad(n)
        contin(x)
    elif choice == 11:
        x = cal.pie()
        contin(x)
    elif choice == 12:
        n = float(input("Enter a number to find its Sine in degrees : "))
        x = cal.sindeg(n)
        contin(x)
    elif choice == 13:
        n = float(input("Enter a number to find its Cosine in degrees : "))
        x = cal.cosdeg(n)
        contin(x)
    elif choice == 14:
        n = float(input("Enter a number to find its Tan in degrees : "))
        x = cal.tandeg(n)
        contin(x)
    elif choice == 15:
        n = float(input("Enter a number to find its Cosecant in degrees : "))
        x = cal.cosecdeg(n)
        contin(x)
    elif choice == 16:
        n = float(input("Enter a number to find its Secant in degrees : "))
        x = cal.secdeg(n)
        contin(x)
    elif choice == 17:
        n = float(input("Enter a number to find its Cot in degrees : "))
        x = cal.cotdeg(n)
        contin(x)
    elif choice == 18:
        n = float(input("Enter a number to find its Natural in log : "))
        x = cal.ln(n)
        contin(x)
    elif choice == 19:
        n = float(input("Enter a number to find its Base 10 log : "))
        x = cal.logten(n)
        contin(x)
    elif choice == 20:
        n1 = float(input("Enter base value : "))
        n2 = float(input("Enter a number to find its log to the given log value : "))
        x = cal.logbasex(n1, n2) # steps are made like functions
        contin(x)
    elif choice == 21:
        n = float(input("Enter a number to get it's Square root : "))
        x = cal.squareroot(n)
        contin(x)
    elif choice == 22:
        n1 = float(input("Enter a number : "))
        n2 = float(input("Enter its power"))
        x = cal.powerof(n1, n2)
        contin(x)
    else:
        print("ERROR : Please enter a valid number ")
