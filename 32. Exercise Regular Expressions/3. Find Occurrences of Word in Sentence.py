import re
line = input().lower()
word = input().lower()

pattern = rf"\b{word}\b"

matches = re.findall(pattern, line)

print(len(matches))