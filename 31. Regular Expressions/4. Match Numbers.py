import re

numbers = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, numbers)

for res in matches:
    print(res.group(), end=' ')


