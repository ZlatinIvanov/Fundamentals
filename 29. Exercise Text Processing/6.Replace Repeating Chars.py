line = input()
result = line[0]
for char in line:
    if char == result[-1]:
        continue
    result += char

print(result)