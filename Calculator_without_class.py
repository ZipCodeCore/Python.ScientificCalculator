import math

def calc(term):
    """
    The term will be the input from the calculator.
    Output will be result of computed term.
    This is where the functions will actually calculate.
    """

    term = term.replace(' ','')     # gets rid of spaces
    term = term.replace('^','**')   # to power of sign recognized as **
    term = term.replace('=','')
    term = term.replace('?','')
    term = term.replace('%','/100') # for percentages
    term = term.replace('rad','radians')
    term = term.replace('mod','%')  # for modula

    functions = ['sin', 'cos', 'tan', 'cosh', 'sinh', 'tanh', 'sqrt', 'pi', 'radians', 'e', 'square', 'exp','factorial']

    term = term.lower()     # convert to lowercase for case sensitive

    for function in functions:
        if function in term:
            usemath = 'math.' + function   # will source the function and combine with math. to create math function
            term = term.replace(function , usemath)

    try:
        term = eval(term)

    except ZeroDivisionError:       # builds in zero division error
        print("Sorry it is not possible to divide by zero! Try again my friend.")
    except NameError:
        print("Sorry that input is not valid! Try again my friend.")
    except AttributeError:
        print("Incorrect usage method! Try again my friend.")
    return(term)

def result(term):  # This passes the argument 'term' to the function 'calc' and prints the result

    print("\n" + str(calc(term)))

def intro():
    """This is for handling the user data and printing the introduction and input
    """
    while True:
        print("\n BOO!! Welcome to the Halloween Scientific Calculator!! Input in any format, enter 'quit' to escape!!")
        answer = input("\n What do you want to know? ")

        if answer == 'quit':
            break
        result(answer)

intro()