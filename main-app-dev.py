from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def getOneNumber():     # get one number instead
    a = float(input("first number? "))
    return a


def displayResult(temp_display: float):
    print("DISPLAY:\n")
    print(temp_display)


def performCalcLoop(calc):


        print('\nBOO! Happy Halloween ;) \n\n "Welcome to your Scientific Calculator."')
        print("\nHere's a list of choices:")
        print('~' * 70)
        print("1 : Addition  \t\t               12 : ")
        print("2 : Subtraction \t               13 : ")
        print("3 : Multiplication\t               14 : ")
        print("4 : Division  \t\t               15 : ")
        print("5 : Square     \t                   16 : ")
        print("6 : Square Root\t                   17 : ")
        print("7 : Variable Exponentiation \t   18 : ")
        print("8 : Inverse of Display  \t       19 : ")
        print("9 : Invert Sign (+/-)\t           20 : Quit")
        print("10 : \t                           21 : ")
        print("11 :  \t\t                       22 : ")
        print('~' * 70)
        temp_display = 0
        print("DISPLAY:")
        print(temp_display)

        while True:
            try:

                choice = input("\nEnter number to choose your operation: \n")
            except:
                print("Please enter a valid number.")

            if choice == '20':
                print("Thanks for stopping by, have a great day.")
                break  # user types q to quit calulator.

            elif choice == '1':
                a, b = getTwoNumbers()
                temp_display = calc.add(a, b)
                displayResult(temp_display)

            elif choice == '2':
                a, b = getTwoNumbers()
                temp_display = calc.sub(a, b)
                displayResult(temp_display)

            elif choice == '3':
                a, b = getTwoNumbers()
                temp_display = calc.mult(a, b)
                displayResult(temp_display)

            elif choice == '4':
                a, b = getTwoNumbers()
                if b == 0:
                    print("Err")
                else:
                    temp_display = calc.div(a, b)
                    displayResult(temp_display)

            elif choice == '5':
                a = getOneNumber()
                temp_display = calc.sq(a)
                displayResult(temp_display)

            elif choice == '6':
                a = getOneNumber()
                temp_display = calc.sqrt(a)
                displayResult(temp_display)

            elif choice == '7':
                a, b = getTwoNumbers()
                temp_display = calc.varexp(a, b)
                displayResult(temp_display)

            elif choice == '8':
                a = getOneNumbers()
                temp_display = calc.inverse(a)
                displayResult(temp_display)

            elif choice == '9':
                a = getOneNumber()
                temp_display = calc.invert_sign(a)
                displayResult(temp_display)

            else:
                print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
