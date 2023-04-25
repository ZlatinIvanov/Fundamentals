string_line = input()
splitted = string_line.split(">")
power = 0
result = [splitted[0]]

for exp in splitted[1:]:
    number_as_str = ""
    for ch in exp:
        if ch.isdigit():
            number_as_str += ch
        else:
            break
    strength = int(number_as_str)
    power += strength

    formatted_part = exp[power:]
    power = max(power - len(exp), 0)
    result.append(formatted_part)

print(">".join(result))
# abv>1>1>2>2asdasd
