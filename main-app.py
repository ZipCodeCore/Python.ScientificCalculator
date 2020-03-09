import math
import decimal

mem = 0

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
       switchdisplaymode(y)
    elif cont == 2:
        fun = int(input("1 : Addition \t\t 2 : Subtraction\n3 : Multiplication \t 4 : Division\n5 : Square root \t 6 : Squared\n7:  Invert Sign\n"))
        contined(fun,y)
    else:
        print("Sorry try again")
        contin(y)

def contined(picked,y):
    if picked == 1:
        x = input("What number would you like to add?\n")
        num2 = test_answer(x,"add", "next")
        z = cal.add(int(y),int(num2))
        contin(z)
    elif picked == 2:
        x = input("What number would you like to subtract?\n")
        num2 = test_answer(x, "subtract", "next")
        z = cal.sub(int(y),int(num2))
        contin(z)
    elif picked == 3:
        x = input("What number would you like to multiply by?\n")
        num2 = test_answer(x, "multiply by", "next")
        z = cal.mul(int(y), int(num2))
        contin(z)
    elif picked == 4:
        x = input("What number would you like to divide by?\n")
        num2 = test_answer(x, "divide by", "next")
        z = cal.div(int(y), int(num2))
        contin(z)
    elif picked == 5:
        z = cal.squareroot(int(y))
        contin(z)
    elif picked == 6:
        z = cal.square(int(y))
        contin(z)
    elif picked == 7:
        z = y*-1
        print (z)
        contin(z)

def switchdisplaymode(x):
    displaypick = int(input("What display would you like to use?\n 1. Binary\n 2. Octal\n 3. Decimal\n 4. Hexadecimal\n 5. Continue to Memory \n"))
    convertdisplay(displaypick,x)

def convertdisplay(l,ber):
    ber = int(ber)
    if l == 1:
        b = bin(ber)
        print(b)
        switchdisplaymode(ber)
    if l == 2:
        b = oct(ber)
        print(b)
        switchdisplaymode(ber)
    if l == 3:
        b = decimal.Decimal(ber)
        print(b)
        switchdisplaymode(ber)
    if l == 4:
        b = hex(ber)
        print(b)
        switchdisplaymode(ber)
    if l == 5:
        memory_ask(ber)

def memory_clear():
    global mem
    mem = 0
    print_options()
def memory_recall():
    global mem
    print(str(mem) + " is in memory")
    int(mem)
    print_options()

def print_options():
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
    print("MRC : To recall memory    M+ : To use number stored in memory")
    print("MC : to Clear Memory      ^C : to Power off   ")
    print('-' * 20)


def memory_ask(x):
    response = input("Would you like to stor this number in memory? Y/N\n")
    if response == "Y":
        global mem
        mem = x
        print_options()
    elif response== "N":
        cal = Calculator()
        print_options()
    else:
        memory_ask(x)




def memory_use(memory):
    global mem
    print(str(mem) + " in memory")
    mem = int(mem)
    choice = ""
    print_options()
    choice = ""
    try:
        choice = input("Enter the number of choice: ")
        if choice == "MC" or choice == "M+" or choice == "MRC":
            str(choice)
        else:
            choice = int(choice)
    except ValueError:
        print("Enter a valid number: ")
    if choice == 1:
        y = input("Enter the second number to add : ")
        n2 = test_answer(y, "to add", "second")
        x = cal.add(mem, n2)
        contin(x)
    elif choice == 2:
        n1 = mem
        y = input("Enter the second number to subtract : ")
        n2 = test_answer(y, "to subtract", "second")
        x = cal.sub(mem, n2)
        contin(x)
    elif choice == 3:
        n1 = mem
        y = input("Enter the second number to multiply : ")
        n2 = test_answer(y,"to multiply","second")
        x = cal.mul(mem, n2)
        contin(x)
    elif choice == 4:
        n1 = memory
        y = input("Enter the second number for division : ")
        n2 = test_answer(y,"for division", "second")
        x = cal.div(mem, n2)
        contin(x)
    elif choice == 5:
        n = mem
        x = cal.sinrad(n)
        contin(x)
    elif choice == 6:
        n = memory
        x = cal.cosrad(n)
        contin(x)
    elif choice == 7:
        n = memory
        x = cal.tanrad(n)
        contin(x)
    elif choice == 8:
        n = memory
        x = cal.cosecrad(n)
        contin(x)
    elif choice == 9:
        n = memory
        x = cal.secrad(n)
        contin(x)
    elif choice == 10:
        n = memory
        x = cal.cotrad(n)
        contin(x)
    elif choice == 11:
        x = cal.pie()
        contin(x)
    elif choice == 12:
        n = memory
        x = cal.sindeg(n)
        contin(x)
    elif choice == 13:
        n = memory
        x = cal.cosdeg(n)
        contin(x)
    elif choice == 14:
        n = memory
        x = cal.tandeg(n)
        contin(x)
    elif choice == 15:
        n = memory
        x = cal.cosecdeg(n)
        contin(x)
    elif choice == 16:
        n = memory
        x = cal.secdeg(n)
        contin(x)
    elif choice == 17:
        n = memory
        x = cal.cotdeg(n)
        contin(x)
    elif choice == 18:
        n = memory
        x = cal.ln(n)
        contin(x)
    elif choice == 19:
        n = memory
        x = cal.logten(n)
        contin(x)
    elif choice == 20:
        n1 = memory
        n2 = input("Enter a number to find its log to this given log value : ")
        x = cal.logbasex(n1, n2) # steps are made like functions
        contin(x)
    elif choice == 21:
        n = memory
        x = cal.squareroot(n)
        contin(x)
    elif choice == 22:
        n1 = memory
        y = input("Enter a number to serve as exponent : ")
        n2 = test_answer(y, "Enter a number to serve as exponent", "")
        x = cal.powerof(n1, n2)
        int(x)
        contin(x)
    elif choice == "MC":
        memory_clear()
    elif choice == "M+":
        mem
        int(mem)
        memory_use(mem)
    elif choice == "MRC":
        memory_recall()
    else:
        print("ERROR : Please enter a valid number")

def test_answer(x, funct, place):
    while type(x) == str:
        try:
            x  = float(x)
        except ValueError:
            print("Error: Please Enter Valid number")
            x = input("Enter " + place + " number to " + funct + ":\n")
    return float(x)









print_options()
choice = ""
while True:
    try:
        choice = input("Enter the number of choice: ")
        if choice == "MC" or choice == "M+" or choice == "MRC":
            pass
        else:
            choice = int(choice)
    except ValueError:
        print("ERROR : Please enter a valid number")
    if choice == 1:
        function_string = "add"
        z = input("Enter the first number to add : ")
        n1 = test_answer(z,function_string,"first")
        y = input("Enter the second number to add : ")
        n2 = test_answer(y,function_string, "second")
        x = cal.add(n1, n2)
        contin(x)
    elif choice == 2:
        function_string = "subtract"
        z = input("Enter the first number in subtraction : ")
        n1 = test_answer(z, function_string, "first")
        y = input("Enter the second number in subraction : ")
        n2 = test_answer(y, function_string, "second")
        x = cal.sub(n1, n2)
        contin(x)
    elif choice == 3:
        function_string = "multiply by"
        z = input("Enter the first number to " + function_string+ " : ")
        n1 = test_answer(z, function_string, "first")
        y = input("Enter the second number number to " + function_string+ " : ")
        n2 = test_answer(y, function_string, "second")
        x = cal.mul(n1, n2)
        contin(x)
    elif choice == 4:
        function_string = "divide by"
        z = input("Enter the first number to " + function_string + " : ")
        n1 = test_answer(z, function_string, "first")
        y = input("Enter the second number number to " + function_string + " : ")
        n2 = test_answer(y, function_string, "second")
        x = cal.div(n1, n2)
        contin(x)
    elif choice == 5:
        function_string = "find Sine its in Radian"
        z = input("Enter a number to "+ function_string + " : ")
        n = test_answer(z,function_string,"")
        x = cal.sinrad(n)
        contin(x)
    elif choice == 6:
        function_string = "find its Cos in radians"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.cosrad(n)
        contin(x)
    elif choice == 7:
        function_string = "find its Tan in radians"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.tanrad(n)
        contin(x)
    elif choice == 8:
        function_string = "find its Cosecant in radians"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.cosecrad(n)
        contin(x)
    elif choice == 9:
        function_string = "find its Secant in radians"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.secrad(n)
        contin(x)
    elif choice == 10:
        function_string = "find its Cot in radians"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.cotrad(n)
        contin(x)
    elif choice == 11:
        x = cal.pie()
        contin(x)
    elif choice == 12:
        function_string = "find its Sine in degrees"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.sindeg(n)
        contin(x)
    elif choice == 13:
        function_string = "find its Cosine in degrees"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.cosdeg(n)
        contin(x)
    elif choice == 14:
        function_string = "find its Tan in degrees"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.tandeg(n)
        contin(x)
    elif choice == 15:
        function_string = "find its Cosecant in degrees"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.cosecdeg(n)
        contin(x)
    elif choice == 16:
        function_string = "find its Secant in degrees"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.secdeg(n)
        contin(x)
    elif choice == 17:
        function_string = "find its Cot in degrees"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.cotdeg(n)
        contin(x)
    elif choice == 18:
        function_string = "find its Natural in log"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.ln(n)
        contin(x)
    elif choice == 19:
        function_string = "find its Base 10 log"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.logten(n)
        contin(x)
    elif choice == 20:
        z = input("Enter base value : ")
        n1 = test_answer(z, "use as base value", "")
        n2 = input("Enter a number to find its log to this given log value : ")
        n2 = test_answer(y, "to serve as the exponent in log function", "")
        x = cal.logbasex(n1, n2)
        contin(x)
    elif choice == 21:
        function_string = "find its square root"
        z = input("Enter a number to " + function_string + " : ")
        n = test_answer(z, function_string, "")
        x = cal.squareroot(n)
        contin(x)
    elif choice == 22:
        z = input("Enter base value : ")
        n1 = test_answer(z, "use as base value", "")
        y = input("Enter a number to serve as exponent : ")
        n2 = test_answer(y, "Enter a number to serve as exponent", "")
        x = cal.powerof(n1, n2)
        contin(x)
    elif choice == "MC":
        memory_clear()
    elif choice == "M+":
        mem
        int(mem)
        memory_use(mem)
    elif choice == "MRC":
        memory_recall()
    else:
        pass