from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("Number? "))
    return a

def switchDisplayModeInput():
    """
    Switch display mode (binary, octal, decimal, hexadecimal)
    switchDisplayMode() should rotate through the options
    :return:
    """
    return str(input('Select a display mode - bin, oct, dec, hex: '))

def trig_units_mode_input():
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
    print("1 : Addition  \t\t               17 : Inverse sine")
    print("2 : Subtraction \t               18 : Inverse cosine")
    print("3 : Multiplication\t               19 : Inverse tangent")
    print("4 : Division  \t\t               20 : Trig units mode - Convert Radians to Degrees")
    print("5 : Square     \t                   21 : Trig units mode - Convert Degrees to Radians")
    print("6 : Square Root\t                   22 : Factorial")
    print("7 : Variable Exponentiation \t   23 : Log x")
    print("8 : Inverse of Display  \t       24 : 10 power x - Inverse nog")
    print("9 : Invert Sign (+/-)\t           25 : Ln x - Natural log")
    print("10 : Switch Display\t               26 : e power x - Inverse natural log")
    print("11 : M+ \t                       27 : Pi")
    print("12 : MC \t                       28 : Exponentiation constant")
    print("13 : MRC \t                       29: Clear")
    print("14 : Sine\t                       30: Quit")
    print("15 : Cosine")
    print("16 : Tangent")
    print('~' * 70)

    temp_display = 0
    print("DISPLAY:")
    print(temp_display)

    memory = 0.0

    while True:

        try:
            choice = input("Enter number to choose your operation:\n")

        except:
            print("Please enter a valid number.")

        if choice == '30':
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
                temp_display = "Err"
                displayResult(temp_display)
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



        elif choice == '10':

            a = switchDisplayModeInput()
            displayResult(calc.switchDisplayMode(a, temp_display))

        elif choice == '11':
            displayResult(calc.madd(temp_display, memory))
            memory = calc.madd(temp_display, memory)


        elif choice == '12':
            displayResult(calc.mclear())
            memory = calc.mclear()


        elif choice == '13':
            displayResult(memory)


        elif choice == '14':
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.sin_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.sin_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '15':
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


        elif choice == '16':
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

        elif choice == '17':
            a = trig_units_mode_input()
            x = getOneNumber()
            if a == 'deg':
                temp_display = calc.inv_sin_deg(x)
                displayResult(temp_display)
            elif a == 'rad':
                temp_display = calc.inv_sin_rad(x)
                displayResult(temp_display)
            else:
                print("That is not a valid input.")


        elif choice == '18':
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


        elif choice == '19':
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

        elif choice == '20':
            x = getOneNumber()
            temp_display = calc.trig_units_mode_deg_to_rad(x)
            print(displayResult(temp_display), " radians")

        elif choice == '21':
            x = getOneNumber()
            temp_display = calc.trig_units_mode_rad_to_deg(x)
            print(displayResult(temp_display), " degrees")

        elif choice == '22':
            x = getOneNumber()
            temp_display = calc.factorial(x)
            print(displayResult(temp_display))

        elif choice == '23':
            print("Enter your number and base as prompted below\n")
            x, b = getTwoNumbers()
            temp_display = calc.log(x, b)
            print(displayResult(temp_display))

        elif choice == '24':
            x = getOneNumber()
            temp_display = calc.inverse_log(x)
            print(displayResult(temp_display))

        elif choice == '25':
            x = getOneNumber()
            temp_display = calc.ln(x)
            print(displayResult(temp_display))

        elif choice == '26':
            x = getOneNumber()
            temp_display = calc.inv_ln(x)
            print(displayResult(temp_display))

        elif choice == '27':
            temp_display = calc.pi()
            displayResult(temp_display)

        elif choice == '28':
            temp_display = calc.e()
            displayResult(temp_display)

        elif choice == '29':
            temp_display = 0
            displayResult(temp_display)

        else:
            print("That is not a valid input.")
            displayResult(temp_display)


def main():
    calc = Calculator()
    performCalcLoop(calc, 0)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
