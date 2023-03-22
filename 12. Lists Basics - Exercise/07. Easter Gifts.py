names_of_gifts = input().split()
is_valid = True
number = 0
inx_c = 0
helper_element = ""
inx_to_remove = 0
while True:
    commands = input().split()
    for c in range(len(commands)):
        if c == 2:
            inx_c = int(commands[2])
        if c == 1:
            helper_element = commands[1]
    if "No" in commands and "Money" in commands:
        is_valid = False
        break
    if "OutOfStock" in commands:
        for j in range(len(names_of_gifts)):
            if names_of_gifts[j] == helper_element:
                names_of_gifts[j] = None
    if "Required" in commands:
        if inx_c >= len(names_of_gifts) or inx_c < 0:
            continue
        else:
            names_of_gifts[inx_c] = helper_element
    if "JustInCase" in commands:
        names_of_gifts.remove(names_of_gifts[-1])
        names_of_gifts.append(commands[1])
final_list = []
for item in names_of_gifts:
    if item != None:
        final_list.append(item)

print(" ".join([str(x) for x in final_list]))
