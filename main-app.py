from calculator import Calculator
import decimal
import math

global mem
mem = 0

def getFirstNumber():
    a = input("first number? ")
    while type(a) == str:
        try:
            a  = float(a)
        except ValueError:
            print("Error: Please Enter Valid number\n")
            a = getFirstNumber()
    return a

def getSecondNumber():
    b = input("second number? ")
    while type(b) == str:
        try:
            b  = float(b)
        except ValueError:
            print("Error: Please Enter Valid number\n")
            b = getSecondNumber()
    return b

def getTwoNumbers():
    a = getFirstNumber()
    b = getSecondNumber()
    return a, b


def displayResult(x: float):
    print(x, "\n")
    return x

def printOptions():
    print("List of choice:")
    print('-' * 60)
    print("Add\t  \t\t   Sine in degrees")
    print("Subtract   \t \t   Cosine in degrees")
    print("Multipy \t \t   Tan in degrees")
    print("Division \t\t   Cosecant in degrees")
    print("Sine in radians \t   Secant in degrees")
    print("Cosine in radians \t   Cotangent in degrees")
    print("Tangent in radians \t   Natural log")
    print("Cosecant in radians  \t   Base 10 log")
    print("Secant in radians \t   Log base'x'")
    print("Cotangent in radians \t   Square root")
    print("Squared \t\t   Exponent")
    print("Inverse \t\t   Switch sign")
    print("Factorial \t\t")
    print("B : For Binary View \t   O : For Octal View")
    print("D : For Decimal View\t   H : For Hexidecimal View")
    print("R: Degree to Radians\t   D: Radians to Degrees")
    print("M+ : Add to Memory   MRC : Add Memory to Display")
    print("MRC: Set Memory to 0")
    

def performFirstCalcLoop(calc):
    while True:
        printOptions()
        print("q to quit")
        print('-' * 60)
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'Add':
            a, b = getTwoNumbers()
            x = displayResult(calc.add(a, b))

        elif choice == 'Subtract':
            a, b = getTwoNumbers()
            x = displayResult(calc.sub(a, b))

        elif choice == 'Multiply':
            a, b = getTwoNumbers()
            x = displayResult(calc.mul(a, b))

        elif choice == 'Division':
            a, b = getTwoNumbers()
            if b != 0:
                x = displayResult(calc.div(a, b))
            else:
                print("Cannot Divide by zero")
                performFirstCalcLoop(calc)

        elif choice == 'Exponent':
            print("First number is base, Second is Exponent")
            a, b = getTwoNumbers()
            x = displayResult(calc.powerof(a, b))

        elif choice == 'Squared':
            a = getFirstNumber()
            x  = displayResult(calc.square(a))

        elif choice == 'Square root':
            a  = getFirstNumber()
            x = displayResult(calc.squareroot(a))

        elif choice == 'Inverse':
            a  = getFirstNumber()
            x = displayResult(calc.inverse(a))

        elif choice == 'Switch sign':
            a  = getFirstNumber()
            x = displayResult(calc.switchsign(a))

        elif choice == 'Sine in radians':
            a  = getFirstNumber()
            x = displayResult(calc.sinrad(a))

        elif choice == 'Cosine in radians':
            a  = getFirstNumber()
            x = displayResult(calc.cosrad(a))


        elif choice == 'Tangent in radians':
            a  = getFirstNumber()
            x = displayResult(calc.tanrad(a))

        elif choice == 'Cosecant in radians':
            a  = getFirstNumber()
            x = displayResult(calc.cosecrad(a))

        elif choice == 'Secant in radians':
            a  = getFirstNumber()
            x = displayResult(calc.secrad(a))

        elif choice == 'Cotangent in radians':
            a  = getFirstNumber()
            x = displayResult(calc.cotrad(a))

        elif choice == 'Sine in degrees':
            a  = getFirstNumber()
            x =displayResult(calc.sindeg(a))

        elif choice == 'Cosine in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.cosdeg(a))

        elif choice == 'Tangent in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.tandeg(a))

        elif choice == 'Cosecant in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.cosecdeg(a))

        elif choice == 'Secant in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.secdeg(a))

        elif choice == 'Cotangent in degrees':
            a  = getFirstNumber()
            x = displayResult(calc.cotdeg(a))

        elif choice == 'Factorial':
            a  = getFirstNumber()
            x = displayResult(calc.factorial(a))

        elif choice == 'Natural log':
            a  = getFirstNumber()
            x = displayResult(calc.ln(a))

        elif choice == 'Base 10 log':
            a  = getFirstNumber()
            x = displayResult(calc.logten(a))

        elif choice == 'Log base x':
            print("Second number is log base")
            a, b = getTwoNumbers()
            x = displayResult(calc.logbasex(a,b))
        elif choice == 'B':
            a = getFirstNumber()
            x = displayResult(bin(int(a)))
            x = a

        elif choice == 'O':
            a = getFirstNumber()
            x = displayResult(oct(int(a)))
            x = a

        elif choice == 'D':
            a = getFirstNumber()
            x = displayResult(decimal.Decimal(a))
            x = a

        elif choice == 'H':
            a = getFirstNumber()
            x = displayResult(hex(int(a)))
            x = a

        elif choice == 'R':
            a = getFirstNumber()
            x = displayResult(math.degrees(a))

        elif choice == 'D':
            a = getFirstNumber()
            x = displayResult(math.radians(a))

        elif choice == 'M+':
            global mem
            mem = x

        elif choice == "MC":
            mem = 0

        elif choice == "MRC":
            x = mem

        else:
            print("That is not a valid input.")
            performFirstCalcLoop(calc)

        performCalcLoop(calc, x)

def performCalcLoop(calc,a):
    x = a
    while True:
        printOptions()

        print("c to clear")
        print('-' * 60)
        print(str(a) + " is your first number\n")
        choice = input("Operation? ")
        if choice == 'c':
            break  # user types q to quit calulator.
        elif choice == 'Add':
            b = getSecondNumber()
            x = displayResult(calc.add(a, b))

        elif choice == 'Subtract':
            a, b = getTwoNumbers()
            x = displayResult(calc.sub(a, b))

        elif choice == 'Multiply':
            b = getSecondNumber()
            x = displayResult(calc.mul(a, b))

        elif choice == 'Division':
            b = getSecondNumber()
            if b != 0:
                x = displayResult(calc.div(a, b))
            else:
                print("Cannot Divide by Zero")
                performCalcLoop(calc,a)

        elif choice == 'Exponent':
            print("First number is base, Second is Exponent")
            b = getSecondNumber()
            x = displayResult(calc.powerof(a, b))

        elif choice == 'Squared':
            x  = displayResult(calc.square(a))

        elif choice == 'Square root':
            a  = getFirstNumber()
            x = displayResult(calc.squareroot(a))

        elif choice == 'Inverse':
            x = displayResult(calc.inverse(a))

        elif choice == 'Switch sign':
            x = displayResult(calc.switchsign(a))

        elif choice == 'Sine in radians':
            x = displayResult(calc.sinrad(a))

        elif choice == 'Cosine in radians':
            x = displayResult(calc.cosrad(a))


        elif choice == 'Tangent in radians':
            x = displayResult(calc.tanrad(a))

        elif choice == 'Cosecant in radians':
            x = displayResult(calc.cosecrad(a))

        elif choice == 'Secant in radians':
            x = displayResult(calc.secrad(a))

        elif choice == 'Cotangent in radians':
            x = displayResult(calc.cotrad(a))

        elif choice == 'Sine in degrees':
            x =displayResult(calc.sindeg(a))

        elif choice == 'Cosine in degrees':
            x = displayResult(calc.cosdeg(a))

        elif choice == 'Tangent in degrees':
            x = displayResult(calc.tandeg(a))

        elif choice == 'Cosecant in degrees':
            x = displayResult(calc.cosecdeg(a))

        elif choice == 'Secant in degrees':
            x = displayResult(calc.secdeg(a))

        elif choice == 'Cotangent in degrees':
            x = displayResult(calc.cotdeg(a))

        elif choice == 'Factorial':
            x = displayResult(calc.factorial(a))

        elif choice == 'Natural log':
            x = displayResult(calc.ln(a))

        elif choice == 'Base 10 log':
            x = displayResult(calc.logten(a))

        elif choice == 'B':
            x = displayResult(bin(int(a)))
            x = a

        elif choice == 'O':
            x = displayResult(oct(int(a)))
            x = a

        elif choice == 'D':
            x = displayResult(decimal.Decimal(a))
            x = a

        elif choice == 'H':
            x = displayResult(hex(int(a)))
            x = a

        elif choice == 'R':
            x = displayResult(math.degrees(a))

        elif choice == 'D':
            x = displayResult(math.radians(a))

        elif choice == 'M+':
            global mem
            mem = x

        elif choice == "MC":
            mem = 0

        elif choice == "MRC":
            x = mem

        elif choice == 'Log base x':
            print("Second number is log base")
            b = getSecondNumber()
            x = displayResult(calc.logbasex(a,b))

        else:
            print("That is not a valid input.")

        performCalcLoop(calc, x)

# main start
def main():
    calc = Calculator()
    performFirstCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()