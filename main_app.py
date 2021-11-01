from calculator import Calculator
import math

calc = Calculator()








def enter_num():
    try:
        num1 = float(input())
        return num1
    except:
        calc.err()



##Calculator Options

def screen_options():
    print("1: Add           8: Inverse              15: M+")
    print("2: Subtract      9: Sine                 16: MC")
    print("3: Multiply      10: Cosine              17: MRC")
    print("4: Divide        11: Tangent             18: Swap")
    print("5: Square        12: Inverse Sine        19: Pi")
    print("6: Square Root   13: Inverse Consine     20: Evaluate")
    print("7: Exponent      14: Inverse Tangent     21: Exit")
    print("")
    Operation = int(input("Choose an operation: (Select the number) "))

    memStore = None

    if Operation == 1:
        print("Add")
        print("Enter the first number: ")
        x = enter_num()
        print("Enter the second number: ")
        y = enter_num()
        calc.result = calc.add(x ,y)
        return calc.result

    elif Operation == 2:
        print("Subtract")
        print("Enter the first number: ")
        x = enter_num()
        print("Enter the second number: ")
        y = enter_num()
        calc.result = calc.subtract(x, y)
        return calc.result

    elif Operation == 3:
        print("Multiply")
        print("Enter the first number: ")
        x = enter_num()
        print("Enter the second number: ")
        y = enter_num()
        calc.result = calc.multiply(x, y)
        return calc.result

    elif Operation == 4:
        print("Divide")
        print("Enter the first number: ")
        x = enter_num()
        print("Enter the second number: ")
        y = enter_num()
        if y == 0:
            print("ERROR")
            return None
        else:
            calc.result = calc.divide(x, y)
            return calc.result

    elif Operation == 5:
        print("Square")
        print("Enter the number: ")
        base = enter_num()
        calc.result = square(base)
        return calc.result

    elif Operation == 6:
        print("Exponent")
        print("Enter the base number: ")
        x = enter_num()
        print("Enter the exponent")
        y = enter_num()
        calc.result = calc.exp(x, y)
        return calc.result

    elif Operation == 7:
        print("Square Root")
        print("Enter the number: ")
        x = enter_num()
        calc.result = calc.square_root(x)
        return calc.result

    elif Operation == 8:
        print("Inverse")
        print("Enter the number: ")
        x = enter_num()
        calc.result = calc.inv(x)
        return calc.result

##TRIG FUNCTIONS
    ##updated with calcments for degrees and radians

    elif Operation == 9:
        print("Sine")
        if calc.degrees:
            print("Enter a number in degrees to find Sine: ")
        else:
            print("Enter a number in radians to find Sine: ")
        x = enter_num()
        calc.result = calc.sin(x)
        return calc.result


    elif Operation == 10:
        print("Cosine")
        raddeg = int(input("For Radians: Enter 1; For Degrees: Enter 2: "))
        if raddeg == 1:
            print("Enter an angle in Radians to find Cosine: ")
            x = enter_num()
            calc.result = calc.cosine(x)
            return calc.result
        elif raddeg == 2:
            print("Enter an angle in Degrees to find Cosine: ")
            x = enter_num()
            calc.result = calc.cosine(math.degrees(x))
            return calc.result


    elif Operation == 11:
        print("Tangent")
        raddeg = int(input("For Radians: Enter 1; For Degrees: Enter 2: "))
        if raddeg == 1:
            print("Enter an angle in Radians to find Tangent: ")
            x = enter_num()
            calc.result = calc.tangent(x)
            return calc.result
        elif raddeg == 2:
            print("Enter an angle in Degrees to find Tangent: ")
            x = enter_num()
            calc.result = calc.tangent(math.degrees(x))
            return calc.result


    elif Operation == 12:
        print("Inverse Sine")
        raddeg = int(input("For Radians: Enter 1; For Degrees: Enter 2: "))
        if raddeg == 1:
            print("Enter an angle in Radians to find Inverse Sine: ")
            x = enter_num()
            calc.result = calc.inverse_sine(x)
            return calc.result
        elif raddeg == 2:
            print("Enter an angle in Degrees to find Inverse Sine: ")
            x = enter_num()
            result = calc.inverse_sine(math.degrees(x))
            return result

    elif Operation == 13:
        print("Inverse Cosine")
        raddeg = int(input("For Radians: Enter 1; For Degrees: Enter 2: "))
        if raddeg == 1:
            print("Enter an angle in Radians to find Inverse Cosine: ")
            x = enter_num()
            calc.result = calc.inverse_cosine(x)
            return calc.result
        elif raddeg == 2:
            print("Enter an angle in Degrees to find Inverse Cosine: ")
            x = enter_num()
            calc.result = calc.inverse_cosine(math.degrees(x))
            return calc.result

    elif Operation == 14:
        print("Inverse Tangent")
        raddeg = calc.degrees
        if raddeg == 1:
            print("Enter an angle in Radians to find Inverse Tangent: ")
            x = enter_num()
            result = calc.inverse_tangent(calc.result)
            return result
        elif raddeg == 2:
            print("Enter an angle in Degrees to find Inverse Tangent: ")
            x = enter_num()
            calc.result = calc.inverse_tangent(math.degrees(x))
            return calc.result

##MEMORY FUNCTIONS

    elif Operation == 15:
        print("M+")
        calc.stored_number = float(input("Enter a number to store: "))
        print(calc.stored_number)
        return calc.stored_number

    elif Operation == 16:
        print("MC")
        if type(calc.stored_number) != None:
            print(calc.stored_number)

    elif Operation == 17:
        print("MCR")
        store_choice = (input("Do you want to clear memory? Y or N: ")).capitalize()
        if store_choice == "Y":
            calc.stored_number= 0
        else:
            pass
        print(calc.stored_number)
        return calc.stored_number

    elif Operation == 18:
        calc.deg_rad_swap()
        if calc.degrees:
            return ("You are in degrees mode")
        else:
            return ("You are in radiants mode")

    elif Operation == 19:
        print("PI = ")
        return 3.14159265359

    elif Operation == 20:
        print("Evaluate")
        x = str(input("Enter what you would like evaluated: "))
        return calc.eval_function(x)

    elif Operation == 21:
        condi = False
        print("Thank you for pushing my buttons!")

##LOOPING OPERATIONS
###DEF FOR SECONDARY OPERATIONS


def choose_data_type():
    type_choice = int(input("Enter data type: 1. Decimal 2. Hexadecimal 3. Binary 4. Octal "))
    if type_choice == 1:
        print(calc.result)
        return (calc.result)
    elif type_choice == 2:
        print(hex(int(calc.result)))
        return hex(int(calc.result))
    elif type_choice == 3:
        print(bin(int(calc.result)).replace("0b", ""))
        return bin(int(calc.result)).replace("0b", "")
    elif type_choice == 4:
        print(oct(int(calc.resultt)))
        return oct(int(calc.result))


def secondary_operation():
    print("1: Add           5: Square           9: M+")
    print("2: Subtract      6: Square Root      10: MC")
    print("3: Multiply      7: Exponent         11: MRC")
    print("4: Divide        8: Inverse          12: Exit")
    print("")
    Operation = int(input('Choose an operation: '))

    memStore = None

    if Operation == 1:
        print("Add")
        print("Enter number to add: ")
        x = enter_num()
        calc.result = calc.add2(x)
        return calc.result

    elif Operation == 2:
        print("Subtract")
        print("Enter the number to subtract: ")
        x = enter_num()
        calc.result = calc.subtract2(x)
        return calc.result

    elif Operation == 3:
        print("Multiply")
        print("Enter the second number: ")
        x = enter_num()
        calc.result = calc.multiply2(x)
        return calc.result

    elif Operation == 4:
        print("Divide")
        print("Enter the second number: ")
        x = enter_num()
        calc.result = calc.divide2(x)
        return calc.result

    elif Operation == 5:
        print("Square")
        calc.result = calc.square2(calc.result)
        return calc.result

    elif Operation == 6:
        print("Exponent")
        print("Enter the exponent: ")
        x = enter_num()
        calc.result = calc.exp2(x)
        return calc.result

    elif Operation == 7:
        print("Square Root")
        calc.result = calc.square_root2(calc.result)
        return calc.result

    elif Operation == 8:
        print("Inverse")
        calc.result = calc.inv2(calc.result)
        return calc.result

    elif Operation == 9:
        memStore = calc.result
        print(memStore)
        return memStore

    elif Operation == 10:
        if type(memStore) != None:
            print(memStore)
        else:
            print('Empty')

    elif Operation == 11:
        store_choice = (input("Do you want to clear memory? Y or N: ")).capitalize()
        if store_choice == "Y":
            memStore = 0
        else:
            pass
        print(memStore)
        return memStore

    elif Operation == 12:
        condi = False
        print('Goodbye!')


######################################################################
## on screen ##


#loop does not operate correctly while welcome and main are defined as functions, must keep open

print("Welcome to our Calculator!")
print("How can we help you?")
print("")



condi = True
while condi:
    calc.result = screen_options()
    print(f"Result: {calc.result}")
    choose_data_type()
    print("")
    cont = (input("Do you continue with this number? Y or N: ")).capitalize()
    print("")
    if cont == "Y":
        condi2 = True
        while condi2:
            calc.result = secondary_operation()
            print(f"Result: {calc.result}")
            choose_data_type()
            print("")
            cont2 = (input("Do you continue with this number? Y or N: ")).capitalize()
            print("")
            if cont2 == "Y":
                condi2 = True
            else:
                break



if __name__ == '__main__':

    main()
    welcome()

