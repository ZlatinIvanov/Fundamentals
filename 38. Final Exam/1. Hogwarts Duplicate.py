def abjuration(s):
    return s.upper()

def necromancy(s):
    return s.lower()

def illusion(s, index, letter):
    if index >= len(s):
        print("The spell was too weak.")
        return s
    else:
        s = s[:index] + letter + s[index+1:]
        print("Done!")
        return s

def divination(s, first, second):
    if first in s:
        s = s.replace(first, second)
        print(s)
        return s
    else:
        return s

def alteration(s, substring):
    if substring in s:
        s = s.replace(substring, "")
        print(s)
        return s
    else:
        return s

spell = input()
while True:
    command = input().split()
    if command[0] == "Abracadabra":
        break
    elif command[0] == "Abjuration":
        spell = abjuration(spell)
        print(spell)
    elif command[0] == "Necromancy":
        spell = necromancy(spell)
        print(spell)
    elif command[0] == "Illusion":
        try:
            index = int(command[1])
            letter = command[2]
            spell = illusion(spell, index, letter)
        except:
            print("The spell did not work!")
    elif command[0] == "Divination":
        try:
            first = command[1]
            second = command[2]
            spell = divination(spell, first, second)
        except:
            print("The spell did not work!")
    elif command[0] == "Alteration":
        try:
            substring = command[1]
            spell = alteration(spell, substring)
        except:
            print("The spell did not work!")
    else:
        print("The spell did not work!")
