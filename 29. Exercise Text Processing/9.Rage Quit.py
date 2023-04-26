line = input()
line.upper()

digits = []
chars = ""

for char in range(len(line)):
    if line[char].isdigit():
        digits.append(line[char])
        multiplier = int(line[char])
        chars *= multiplier
        digits = [0]
    else:
        chars += line[char]

print(digits)
print(chars)
print(line)