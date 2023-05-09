spell = input()

while True:
    commands = input()
    if commands == "Abracadabra":
        break
    commands = commands.split()
    command = commands[0]
    if command == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif command == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif command == "Illusion":
        inx = int(commands[1])
        letter = commands[2]
        if inx >= len(spell):
            print("The spell was too weak.")
        else:
            spell = spell.replace(spell[inx], letter)
            print("Done!")
    elif command == "Divination":
        first_substr = commands[1]
        second_substr = commands[2]
        if first_substr in spell:
            spell = spell.replace(first_substr, second_substr)
            print(spell)
        else:
            continue
    elif command == "Alteration":
        substring = commands[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
        else:
            continue
    else:
        print("The spell did not work!")
