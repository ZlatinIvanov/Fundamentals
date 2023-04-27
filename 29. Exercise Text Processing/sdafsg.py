# line = input()
line = "A12b"
asd = []
number = 0
for char in line:
    if char.isupper():
        divider = ord(line[0]) - 64
        number = number / divider
    else:
        multiplier = ord(line[0]) - 64
        number = number * multiplier
