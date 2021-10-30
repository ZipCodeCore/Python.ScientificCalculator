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
    elif state.user_entry.upper() == "HELP":
        state.help()
        continue
    elif state.user_entry.upper() == "EXIT":
        break
    else:
        state.command = state.user_entry.upper()
print("thanks for pushing all my buttons")
