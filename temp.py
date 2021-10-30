state = 0
screen_number = 0
command = ""
display_mode = "decimal"

def add(a,b):
    return a + b


def compute_state(screen_number):
        if display_mode == "decimal":
            return str(screen_number)
        elif display_mode == "hex":
            pass


while True:
    state = compute_state(screen_number)
    print("current state:", state)
    user_entry = input("please enter something?")
    if user_entry.isnumeric():
        user_entry = float(user_entry)
        if command == "":
            screen_number = user_entry
        elif command == "add":
            screen_number = add(screen_number,user_entry)
        elif command == "sub":
            sub(screen_number,user_entry)
    elif user_entry == "exit":
        break
    else:
        command = user_entry
print("thanks for pushing all my buttons")
