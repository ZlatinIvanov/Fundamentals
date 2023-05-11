import re
pattern = r"^(\$|%)([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"
nums = int(input())
ascii_convert = []
for n in range(nums):
    message = input()
    matches = re.findall(pattern, message)
    if matches:
        for match in matches:
            ascii_symbols = chr(int(match[2])) + chr(int(match[3])) + chr(int(match[4]))
            print(f"{match[1]}: {ascii_symbols}")
    else:
        print("Valid message not found!")