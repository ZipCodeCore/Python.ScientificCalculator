from calculator import Calculator
import math

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def getOneNumber():     # get one number instead
    a = float(input("first number? "))
    return a

def switchDisplayModeInput(): #added by KB
    """
    Switch display mode (binary, octal, decimal, hexadecimal)
    switchDisplayMode() should rotate through the options
    :return:
    """
    return str(input('Select a display mode - bin, oct, dec, hex: '))

def trig_units_mode_input(): #added by KB
    """
    Switch trig units mode (Degrees, Radians)
    switchUnitsMode() should rotate through the options
    :return:
    """
    return input('Select deg or rad: ')

def displayResult(temp_display: float):
    print("\nDISPLAY:\n")
    print(temp_display)


def performCalcLoop(calc, temp_display): # KB - removed none assignment to temp_display
    print('\nBOO! Happy Halloween ;) \n\n "Welcome to your Scientific Calculator."')
    print("\nHere's a list of choices:")
    print('~' * 70)
    print("1 : Addition  \t\t               12 : MC")
    print("2 : Subtraction \t               13 : MRC")
    print("3 : Multiplication\t               14 : Sine ")
    print("4 : Division  \t\t               15 : Cosine ")
    print("5 : Square     \t                   16 : Tangent ")
    print("6 : Square Root\t                   17 : Inverse Sine")
    print("7 : Variable Exponentiation \t   18 : Inverse Cosine")
    print("8 : Inverse of Display  \t       19 : Inverse Tangent")
    print("9 : Invert Sign (+/-)\t           20 : Quit")
    print("10 : Switch Display\t                           21 : ")
    print("11 : M+ \t\t                       22 : ")
    print('~' * 70)


    while True:
        try:
            choice = input("Enter number to choose your operation:\n")
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



        elif choice == '10': #added by KB
                # switch display
            a = switchDisplayModeInput()
            displayResult(calc.switchDisplayMode(a,temp_display))

        #elif choice == 'M+':
        #elif choice == '11':


        #elif choice == '12''MC':

        #elif choice == '13''MRC':

        elif choice == '14': #added by KB
            a = trig_units_mode_input()
            x=getOneNumber()
            if a == 'deg':
                temp_display = calc.sin_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.sin_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '15':  # added by KB
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.cos_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.cos_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '16':  # added by KB
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.tan_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.tan_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")

        elif choice == '17': #added by KB
            a = trig_units_mode_input()
            x=getOneNumber()
            if a == 'deg':
                temp_display = calc.inv_sin_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.inv_sin_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '18':  # added by KB
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.inv_cos_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.inv_cos_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '19':  # added by KB
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.inv_tan_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.inv_tan_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc, 0) #KB - passed second input parameter 0
    print("Done Calculating.")


if __name__ == '__main__':
    main()