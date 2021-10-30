from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def getOneNumber():     # get one number instead
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
            displayResult(calc.sub(a, b))

        elif choice == 'multiply':
            a, b = getTwoNumbers()
            displayResult(calc.mult(a, b))

        elif choice == 'divide':
            a, b = getTwoNumbers()
            if b == 0:
                print("Err")
            else:
                displayResult(calc.div(a, b))

        elif choice == 'square':
            a = getOneNumber()
            displayResult(calc.sq(a))

        elif choice == 'square root':
            a = getOneNumber()
            displayResult(calc.sqrt(a))

        elif choice == 'variable exponentiation':
            a, b = getTwoNumbers()
            displayResult(calc.varexp(a, b))

        elif choice == 'inverse':
            a = getOneNumbers()
            displayResult(calc.inverse(a))

        elif choice == 'invert sign':
            a = getOneNumber()
            displayResult(calc.invert_sign(a))

        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
