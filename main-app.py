from calculator import Calculator
import math
import decimal

calc=Calculator()

def enter_num():
    num1 = float(input())
    return num1

global mem
mem = 0

def enter_num():
    num1 = float(input())
    return num1

def screen_options():
    print("1: Add           8: Inverse              15: M+")
    print("2: Subtract      9: Sine                 16: MC")
    print("3: Multiply      10: Cosine              17: MRC")
    print("4: Divide        11: Tangent             18: Exit")
    print("5: Square        12: Inverse Sine")
    print("6: Square Root   13: Inverse Consine")
    print("7: Exponent      14: Inverse Tangent")
    print("")
    Operation = int(input('Choose an operation: (Select the number) '))
    memStore = None

    if Operation == 1:
        print("Add")
        print("Enter the first number: ")
        x = enter_num()
        print("Enter the second number: ")
        y = enter_num()
        result = calc.add(x, y)
        return result

    elif Operation == 2:
        print("Subtract")
        print('Enter the first number: ')
        x = enter_num()
        print('Enter the second number: ')
        y = enter_num()
        result = calc.subtract(x, y)
        return result

    elif Operation == 3:
        print('Multiply')
        print('Enter the first number: ')
        x = enter_num()
        print('Enter the second number: ')
        y = enter_num()
        result = calc.multiply(x, y)
        return result

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
            result = calc.divide(x, y)
            return result

    elif Operation == 5:
        print("Square")
        print("Enter the number: ")
        base = enter_num()
        result = square(base)
        return result

    elif Operation == 6:
        print("Exponent")
        print("Enter the base number: ")
        x = enter_num()
        print("Enter the exponent")
        y = enter_num()
        result = calc.exp(x, y)
        return result

    elif Operation == 7:
        print("Square Root")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result

    elif Operation == 8:
        print("Inverse")
        print("Enter the number: ")
        x = enter_num()
        result = calc.inv(x)
        return result

##TRIG FUNCTIONS
##must add statements for degrees/radians

    elif Operation == 9:
        print("Sine")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result


    elif Operation == 10:
        print("Cosine")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result


    elif Operation == 11:
        print("Tangent")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result


    elif Operation == 12:
        print("Inverse Sine")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result

    elif Operation == 13:
        print("Inverse Cosine")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result

    elif Operation == 14:
        print("Inverse Tangent")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result


    elif Operation == 15:
        print("M+")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result


    elif Operation == 16:
        print("MC")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result

    elif Operation == 17:
        print("MCR")
        print("Enter the number: ")
        x = enter_num()
        result = calc.square_root(x)
        return result

    elif Operation == 18:
        condi = False
        print("Thank you for pushing my buttons!")


######################################################################
## on screen ##


print("Welcome to our Calculator!")
print("How can we help you?")
print("")

screen_options()
