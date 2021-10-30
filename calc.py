from calculator import state

state = state()


def add(a,b):
    state.command = None
    return a + b




while True:
    state.print()
    if state.command != None:
        print("current command is:", state.command)
    state.user_entry = input("please enter a mathematical function or number: ")
    if state.user_entry.isnumeric():
        state.user_entry = float(state.user_entry)
        if state.command == None:
            state.value = state.user_entry
        elif state.command == "add":
            state.value = add(state.value,state.user_entry)
        elif state.command == "sub":
            sub(state.value,user_entry)
    elif state.user_entry == "exit":
        break
    else:
        state.command = state.user_entry
print("thanks for pushing all my buttons")
