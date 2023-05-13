string = input()

while True:
    commands = input()
    if commands == "Finish":
        break
    commands = commands.split()
    command = commands[0]
    if command == "Repalce":
        cur_char = commands[1]
        new_char = commands[2]
        if cur_char in string:
            string = string.replace(cur_char, new_char)
    elif command == "Cut":
        start_inx = commands[1]
        end_inx = commands[2]
        string = string[:start_inx] + string[end_inx:]