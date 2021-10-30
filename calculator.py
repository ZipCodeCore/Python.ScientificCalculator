class state:
    """
    initiates a calculator object
    """
    def __init__(self):
        self.value = 0
        self.command = None
        self.display_mode = "decimal"
        self.trig_mode = "rads"
        self.display = "0"
        self.user_entry = None


    def get_current_value(self):
        pass


    def print(self):
        if self.display_mode == "decimal":
            self.display = str(self.value)
        elif self.display_mode == "hex":
            self.display = hex(self.value)
        elif self.display_mode == "binary":
            pass
        elif self.display_mode == "octal":
            pass
        else:
            self.error()
        print("current display is:",self.display)


    def error(self):
        self.value = None
        self.command = None
        self.display_mode = "Err"

    def add(self,n):
        self.value = self.value + n
        self.command = None

    def help(self):
        print("You may enter a number or a command. They command will act on the displayed numnber, or wait for a second number to take action")
        print("the commands are +, -, *, /, Square, SquareRoot, ^, Invert, ClearError, SwitchSign, Decimal, Binary, Octal, Hex, ToggleDisplayStyle, M+, MC, MRC, Sine, Cosine, Tangent, ASine, ACosine, Atangent, SwitchTrigMode, Rads, Degrees, !, Log, 10^x, Ln, e^x")

class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return 0

# add lots more methods to this calculator class.
