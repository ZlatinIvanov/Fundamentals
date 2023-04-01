init_list = input().split("!")

while True:
    commands = input().split()
    if commands[0] == "Go" and commands[1] == "Shopping!":
        break
    if commands[0] == "Urgent":
        if commands[1] in init_list:
            continue
        else:
            init_list.remove(commands[1])
            init_list.insert(0, commands[1])
    if commands[0] == "Unnecessary":
        if commands[1] in init_list:
            init_list.remove(commands[1])
        else:
            continue
    if commands[0] == "Correct":
        for x in range(len(init_list)):
            if init_list[x] == commands[1]:
                init_list[x] = commands[2]
            else:
                continue
    if commands[0] == "Rearrange":
        if commands[1] in init_list:
            init_list.remove(commands[1])
            init_list.append(commands[1])
        pass

print(", ".join(init_list))
