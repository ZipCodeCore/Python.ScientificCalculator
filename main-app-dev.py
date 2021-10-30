from calculator import Calculator
import math


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def getOneNumber():
    a = float(input("first number? "))
    return a


def displayResult(x: float):
    print(x, "\n")


def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            print("Thanks for stopping by, have a great day.")
            break  # user types q to quit calulator.

        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))

        elif choice == 'subtract':
            a, b = getTwoNumbers()
            displayResult(a-b)

        elif choice == 'multiply':
            a, b = getTwoNumbers()
            displayResult(a*b)

        elif choice == 'divide':
            a, b = getTwoNumbers()
            if b == 0:
                print("Err")
            else:
                displayResult(a/b)

# Have to use getOneNumber for certain operations

        elif choice == 'square':
            a = getOneNumber()
            displayResult(a**2)

        elif choice == 'square root':
            a = getOneNumber()
            displayResult(math.sqrt(a))

        elif choice == 'variable exponentiation':
            a, b = getTwoNumbers()
            displayResult(a**b)

        elif choice == 'inverse':
            a = getOneNumbers()
            displayResult(1 / a)

        elif choice == 'invert sign':
            a = getOneNumber()
            displayResult(a * -1)

        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
