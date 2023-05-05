message = input()
letters_to_move = ""
while True:
    commands = input()
    if commands == "Decode":
        break
    commands = commands.split("|")
    instruction = commands[0]
    if instruction == "Move":
        num_letters = int(commands[1])
        message = message[num_letters:] + message[:num_letters]
    if instruction == "Insert":
        inx = int(commands[1])
        value = commands[2]
        message = message[0:inx] + value + message[inx::]
    if instruction == "ChangeAll":
        substr = commands[1]
        replacement = commands[2]
        if substr in message:
            message = message.replace(substr, replacement)

print(f"The decrypted message is: {message}")
