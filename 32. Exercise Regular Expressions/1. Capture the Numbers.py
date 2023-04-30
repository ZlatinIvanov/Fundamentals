import re

result = []
while True:
    line = input()
    if not line:
        break

    pattern = r"\d+"
    matches = re.findall(pattern, line)
    result.extend(matches)

print(" ".join(result))
