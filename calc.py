from calculator import state

state = state()






while True:
    state.print()
    if state.command != None:
        print("current command is:", state.command)
    state.user_entry = input("please enter a mathematical function or number (or type help): ")
    if state.user_entry.isnumeric():
        state.user_entry = float(state.user_entry)
        if state.command == None:
            state.value = state.user_entry
        elif state.command == "+":
            state.add(state.user_entry)
        elif state.command == "-":
            state.sub(state.user_entry)
        elif state.command == "HELP":
            state.help()
    elif state.user_entry == "EXIT":
        break
    else:
        state.command = state.user_entry.capitalize()
print("thanks for pushing all my buttons")
