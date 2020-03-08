from calculator import Calculator

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def getOneNumber():
    a = float(input("Input number? "))
    return a


def switchDisplayUnitMode(displayUnitMode : str):
    global switchUnit
    if displayUnitMode == 'DE':
        switchUnit = 1
        print("Degree")
    elif displayUnitMode == 'RA':
        switchUnit = 2
        print("Radians")

        print(switchUnit)

def switchDisplayMode(displayMode : str):
    global switch_display
    if displayMode == 'B':
        switch_display = 1
        print("Binary")
    elif displayMode == 'O':
        switch_display = 2
        print("Octal")
    elif displayMode == 'H':
        switch_display = 3
        print("HexaDecimal")
    elif displayMode == 'D':
        switch_display = 0
        print("Decimal")



    print(switch_display)


def displayResult(x: float):

    global switch_display
    if switch_display == 1:
        print("Approximate Binary Representation: "+bin(int(x)), "\n")
    elif switch_display == 2:
        print("Approximate Octal Representation: "+oct(int(x)), "\n")
    elif switch_display == 3:
        print("Approximate Hexadecimal Representation: "+hex(int(x)), "\n")
    elif switch_display == 0:

        print(x, "\n")


def performCalcLoop(calc):
    global switchUnit
    while True:
        choice = input("Operation ? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
        elif choice == 'sub':
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b))
        elif choice == 'mul':
            a, b = getTwoNumbers()
            displayResult((calc.mul(a, b)))
        elif choice == 'div':
            a, b = getTwoNumbers()
            displayResult(calc.div(a, b))
        elif choice == 'inverse':
            a = getOneNumber()
            displayResult(calc.inverse(a))
        elif choice == 'invert_sign':
            a = getOneNumber()
            displayResult(calc.invert_sign(a))
        elif choice == 'square':
            a = getOneNumber()
            displayResult(calc.square(a))
        elif choice == 'square_rt':
            a = getOneNumber()
            displayResult(calc.square_rt(a))
        elif choice == 'sdm':
            displayMode = input(" Select Display Mode B:Binary, O:Octal, H:HexaDecimal, D:Decimal ")
            switchDisplayMode(displayMode)
        elif choice == 'cal_sin':
            a = getOneNumber()
            displayResult(calc.cal_sin(a, switchUnit))
        elif choice == 'cal_cosin':
            a = getOneNumber()
            displayResult(calc.cal_cosin(a, switchUnit))
        elif choice == 'cal_tang':
            a = getOneNumber()
            displayResult(calc.cal_tang(a, switchUnit))
        elif choice == 'inverse_sin':
            a = getOneNumber()
            displayResult(calc.inverse_sin(a, switchUnit))
        elif choice == 'stum':
            displayUnitMode = input(" Select Display TRIG Mode DE:Degree, RA:Radians ")
            switchDisplayUnitMode(displayUnitMode)







        else:
            print("That is not a valid input.")



# main start
def main():
    global switch_display
    global switchUnit
    switchUnit = 1
    switch_display = 0
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
