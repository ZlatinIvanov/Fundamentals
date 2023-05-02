import re
new_list = []
pattern = r"(www\.[A-Za-z\d\-]+(\.[a-z]+)+)"

while True:
    line = input()
    if not line:
        break

    matches = re.findall(pattern, line)
    new_list.extend([m[0] for m in matches])

for match in new_list:
    print(match)