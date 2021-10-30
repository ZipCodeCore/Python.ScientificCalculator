from calculator import Calculator
import math
import decimal

global mem
mem = 0

def enter_num():
    num1 = float(input())
    return num1

def screen_options():
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Square")
    print("6: Square Root")
    print("7: Exponent")
    print("8: Exit")
    print("")
    Operation = int(input('Choose an operation: (Select the number) '))
    memStore = None

    if Operation == 1:
        print("Add")
        print("Enter the first number: ")
        x = enter_num()
        print("Enter the second number: ")
        y = enter_num()
        result = add(x, y)
        return result

    elif Operation == 2:
        print("Subtract")
        print('Enter the first number: ')
        x = enter_num()
        print('Enter the second number: ')
        y = enter_num()
        result = subtract(x, y)
        return result

    elif Operation == 3:
        print('Multiply')
        print('Enter the first number: ')
        x = enter_num()
        print('Enter the second number: ')
        y = enter_num()
        result = multiply(x, y)
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
            result = divide(x, y)
            return result

    elif Operation == 5:
        print("Square")
        print('Enter a number to square: ')
        base = enter_num()
        result = square(base)
        return result

    elif Operation == 6:
        print("Exponent")
        print("Enter the base number: ")
        x = enter_num()
        print("Enter the exponent")
        y = enter_num()
        result = exp(x, y)
        return result

    elif Operation == 7:
        print("Square Root")
        print("Enter the number: ")
        x = enter_num()
        result = square_root(x)
        return result

    elif Operation == 8:
        print("Inverse")
        x = enter_num()
        result = inv(x)
        return result

    elif Operation == 8:
        condi = False
        print("Thank you for pushing my buttons!")


######################################################################
## on screen ##


print("Welcome to our Calculator!")
print("How can we help you?")
print("")

screen_options()
