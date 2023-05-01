import re

pattern = f"(\s[A-z0-9][\w\-.]*[A-z0-9]@[A-z][A-z\-]*[A-z][A-z](\.[A-z][A-z\-]*[A-z])+)"

line = input()

match = re.findall(pattern, line)

for data in match:
    print(data[0].strip())

