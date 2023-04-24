line = input()
encrypted = []
result = ""
for char in line:
    char = ord(char) + 3
    encrypted.append(char)
for char in encrypted:
    char = chr(char)
    result += char
print(result)