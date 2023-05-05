import re

pattern = r"^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"
group = re.compile(r"\d")
regex = re.compile(pattern)
numbers = int(input())

for n in range(numbers):
    line = input()
    if regex.match(line):
        digits = group.findall(line)
        if digits:
            product_group = "".join(digits)
        else:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
