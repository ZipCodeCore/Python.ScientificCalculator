from calculator import Calculator


def getTwoNumbers():
    a = float(input("First Number? "))
    b = float(input("Second Number? "))
    return a, b


def getOneNumber():     # get one number instead
    a = float(input("Number? "))
    return a


def displayResult(temp_display: float):
    print("\nDISPLAY:\n")
    print(temp_display)


def performCalcLoop(calc,temp_display):  # KB - removed none assignment to temp_display


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
        print("10 : \t                           21 : Clear")
        print("11 :  \t\t                       22 : ")
        print('~' * 70)
        temp_display = 0
        print("DISPLAY:")
        print(temp_display)

        while True:
            while temp_display == 0:

                try:
                    choice = input("\nEnter number to choose your operation: \n")
                except:
                    print("Please enter a valid number.")

                if choice == '20':
                    print("Thanks for stopping by, have a great day.")
                    break

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
                        print("\nDISPLAY:\nErr")
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
                    a = getOneNumber()
                    temp_display = calc.inverse(a)
                    displayResult(temp_display)

                elif choice == '9':
                    a = getOneNumber()
                    temp_display = calc.invert_sign(a)
                    displayResult(temp_display)

                #elif choice == '21':
                    #displayResult(temp_display)

                else:
                    print("That is not a valid input.")
                    displayResult(temp_display)

            while temp_display != 0:
                try:

                    choice = input("\nEnter number to choose your operation: \n")
                except:
                    print("Please enter a valid number.")

                if choice == '20':
                    print("Thanks for stopping by, have a great day.")
                    break  # user types q to quit calulator.

                elif choice == '1':
                    b = getOneNumber()
                    temp_display = calc.add(temp_display, b)
                    displayResult(temp_display)

                elif choice == '2':
                    b = getOneNumber()
                    temp_display = calc.sub(temp_display, b)
                    displayResult(temp_display)

                elif choice == '3':
                    b = getOneNumber()
                    temp_display = calc.mult(temp_display, b)
                    displayResult(temp_display)

                elif choice == '4':
                    b = getOneNumber()
                    if b == 0:
                        print("\nDISPLAY:\nErr")
                    else:
                        temp_display = calc.div(temp_display, b)
                        displayResult(temp_display)

                elif choice == '5':
                    temp_display = calc.sq(temp_display)
                    displayResult(temp_display)

                elif choice == '6':
                    temp_display = calc.sqrt(temp_display)
                    displayResult(temp_display)

                elif choice == '7':
                    b = getTwoNumbers()
                    temp_display = calc.varexp(temp_display, b)
                    displayResult(temp_display)

                elif choice == '8':
                    temp_display = calc.inverse(temp_display)
                    displayResult(temp_display)

                elif choice == '9':
                    temp_display = calc.invert_sign(temp_display)
                    displayResult(temp_display)

                elif choice == '21':
                    temp_display = 0
                    displayResult(temp_display)

                else:
                    print("That is not a valid input.")
                    displayResult(temp_display)

# main start
def main():
    calc = Calculator()
    performCalcLoop(calc, 0) #KB - passed second input parameter 0
    print("Done Calculating.")


if __name__ == '__main__':
    main()
