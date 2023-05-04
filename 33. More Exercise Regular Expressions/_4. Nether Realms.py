import re

pattern = r""
health_reg = r"[^0-9.*-+\/]"
numbers_reg = r"((-|\+)?)((\d)(.\d+)?)"
multiply_reg = r"*"
divide_reg = r"\\"
line = input().split(", ")
line = sorted(line)
for l in line:
    match = re.findall(health_reg, l.strip())
    health_result = sum([ord(c) for c in match])
    numbers = re.finditer(numbers_reg, l)
    for x in numbers:
        asd = x.group()
print(line)