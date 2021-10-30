from calculator import Calculator
import math
import decimal

calc=Calculator()

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
        result = calc.sine(x)
        return result


    elif Operation == 10:
        print("Cosine")
        print("Enter the number: ")
        x = enter_num()
        result = calc.cosine(x)
        return result


    elif Operation == 11:
        print("Tangent")
        print("Enter the number: ")
        x = enter_num()
        result = calc.tangent(x)
        return result


    elif Operation == 12:
        print("Inverse Sine")
        print("Enter the number: ")
        x = enter_num()
        result = calc.invsine(x)
        return result

    elif Operation == 13:
        print("Inverse Cosine")
        print("Enter the number: ")
        x = enter_num()
        result = calc.invcosine(x)
        return result

    elif Operation == 14:
        print("Inverse Tangent")
        print("Enter the number: ")
        x = enter_num()
        result = calc.invtangent(x)
        return result

##MEMORY FUNCTIONS

    elif Operation == 15:
        print("M+")
        print("Enter the number: ")
        memStore = float(input("Enter a value to store: "))
        print(memStore)
        return memStore


    elif Operation == 16:
        print("MC")
        if type(memStore) != None:
            print(memStore)

    elif Operation == 17:
        print("MCR")
        store_choice = input("Do you want to clear memory? Y or N (case sensitive): ")
        if store_choice == "Y":
            memStore = 0
        else:
            pass
        print(memStore)
        return memStore

    elif Operation == 18:
        condi = False
        print("Thank you for pushing my buttons!")

##LOOPING OPERATIONS
###DEF FOR SECONDARY OPERATIONS


def choose_data_type():
    data_choice = int(input('Enter data type: 1. Decimal 2. Hexadecimal 3. Binary 4. Octal '))
    if data_choice == 1:
        print(returned_result)
        return returned_result
    elif data_choice == 2:
        print(hex(int(returned_result)))
        return hex(int(returned_result))
    elif data_choice == 3:
        print(bin(int(returned_result)).replace("0b", ""))
        return bin(int(returned_result)).replace("0b", "")
    elif data_choice == 4:
        print(oct(int(returned_result)))
        return oct(int(returned_result))


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
        result = calc.add2(x)
        return result

    elif Operation == 2:
        print("Subtract")
        print("Enter the number to subtract: ")
        x = enter_num()
        result = calc.subtract2(x)
        return result

    elif Operation == 3:
        print("Multiply")
        print("Enter the second number: ")
        x = enter_num()
        result = calc.multiply2(x)
        return result

    elif Operation == 4:
        print("Divide")
        print("Enter the second number: ")
        x = enter_num()
        result = calc.divide2(x)
        return result

    elif Operation == 5:
        print("Square")
        result = square2(returned_result)
        return result

    elif Operation == 6:
        print("Exponent")
        print("Enter the exponent: ")
        x = enter_num()
        result = calc.exp2(x)
        return result

    elif Operation == 7:
        print("Square Root")
        result = calc.square_root2(returned_result)
        return result

    elif Operation == 8:
        print("Inverse")
        result = inv2(returned_result)
        return result

    elif Operation == 9:
        memStore = returned_result
        print(memStore)
        return memStore

    elif Operation == 10:
        if type(memStore) != None:
            print(memStore)
        else:
            print('Empty')

    elif Operation == 11:
        store_choice = input("Do you want to clear memory? Y or N (case sensitive): ")
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


print("Welcome to our Calculator!")
print("How can we help you?")
print("")


condi = True
while condi:
    returned_result = screen_options()
    print(f"Result: {returned_result}")
    choose_data_type()
    print("")
    cont = input("Continue with current value? Y or N (case sensitive): ")
    print('')
    if cont == "Y":
        condi2 = True
        while condi2:
            returned_result = secondary_operation()
            print(f"Result: {returned_result}")
            choose_data_type()
            print("")
            cont2 = input("Continue with current value? Y or N (case sensitive): ")
            print("")
            if cont2 == "Y":
                condi2 = True
            else:
                break