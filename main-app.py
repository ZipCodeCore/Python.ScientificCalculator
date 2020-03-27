from calculator import Basic_func
from . import CalculatorMemory

def show_calc_mode_options(calc_options) -> None:

    for key, value in calc_options.items():
        print(f'{key}: {value}')


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


# def performCalcLoop(calc, memory):
#     global switchUnit
#     while True:
#         choice = input("Operation ? ")
#         if choice == 'q':
#             break  # user types q to quit calulator.
#         elif choice == 'add':
#             a, b = getTwoNumbers()
#             calc.state = calc.add(a, b)
#             displayResult(calc.state)
#         elif choice == 'sub':
#             a, b = getTwoNumbers()
#             calc.state = calc.sub(a, b)
#             displayResult(calc.state)
#         elif choice == 'mul':
#             a, b = getTwoNumbers()
#             calc.state = calc.mul(a, b)
#             displayResult(calc.state)
#         elif choice == 'div':
#             a, b = getTwoNumbers()
#             calc.state = calc.div(a, b)
#             displayResult(calc.state)
#         elif choice == 'inverse':
#             a = getOneNumber()
#             calc.state = calc.inverse(a)
#             displayResult(calc.state)
#         elif choice == 'invert_sign':
#             a = getOneNumber()
#             calc.state = calc.invert_sin(a)
#             displayResult(calc.state)
#         elif choice == 'square':
#             a = getOneNumber()
#             calc.state = calc.square(a)
#             displayResult(calc.state)
#         elif choice == 'square_rt':
#             a = getOneNumber()
#             calc.state = calc.square_rt(a)
#             displayResult(calc.state)
#         elif choice == 'sdm':
#             displayMode = input(" Select Display Mode B:Binary, O:Octal, H:HexaDecimal, D:Decimal ")
#             switchDisplayMode(displayMode)
#         elif choice == 'cal_sin':
#             a = getOneNumber()
#             displayResult(calc.cal_sin(a, switchUnit))
#         elif choice == 'cal_cosin':
#             a = getOneNumber()
#             displayResult(calc.cal_cosin(a, switchUnit))
#         elif choice == 'cal_tang':
#             a = getOneNumber()
#             displayResult(calc.cal_tang(a, switchUnit))
#         elif choice == 'inverse_sin':
#             a = getOneNumber()
#             displayResult(calc.inverse_sin(a, switchUnit))
#         elif choice == 'stum':
#             displayUnitMode = input(" Select Display TRIG Mode DE:Degree, RA:Radians ")
#             switchDisplayUnitMode(displayUnitMode)
#         elif choice == 'reset':
#             memory.resetMem()
#         elif choice == 'getMem':
#             displayResult(memory.getLatMemVal()
#          else:
#             print("That is not a valid input.")



# main start
def main():
    # global switch_display
    # global switchUnit
    # switchUnit = 1
    # switch_display = 0
    calc_mode_options = {
        "1":"Basic"
    }
    basic_calc = Basic_func()
    # performCalcLoop(calc)
    # print("Done Calculating.")
    calculator_mode = {
        "1": basic_calc,
        # 2: "Intermediate\n",
        # 3: "Advanced\n"
    }
    print("Please choose a Mode: ")
    show_calc_mode_options(calc_mode_options)



    user_input = input("Enter your choice of mode: ")
    print("Enter function option: ")
    show_calc_mode_options(calculator_mode[str(user_input)].options)
    # global switch_display
    # global switchUnit
    # switchUnit = 1
    # switch_display = 0
    # calc = Calculator(0)
    # memory = CalculatorMemory(0)
    # performCalcLoop(calc, memory)
    # print("Done Calculating.")


if __name__ == '__main__':
    main()
