class state:
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



class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return 0

# add lots more methods to this calculator class.
