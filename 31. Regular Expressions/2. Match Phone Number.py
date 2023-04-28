import re

numbers = input()

pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"

match = re.findall(pattern, numbers)
print(*match, sep=", ")
