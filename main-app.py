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
    print("10 : Switch Display\t              26 : e power x - Inverse natural log")
    print("11 : M+ \t                       27 : Pi")
    print("12 : MC \t                       28 : Exponentiation constant")
    print("13 : MRC \t                       29: Clear")
    print("14 : Sine\t                      30: Quit")
    print("15 : Cosine")
    print("16 : Tangent")
    print('~' * 70)

    temp_display = 0
    print("DISPLAY:")
    print(temp_display)

    memory = 0.0
