import re

pattern_name = r"[A-Za-z]"
pattern_digits = r"\d"
list_of_participants = input().split(", ")
names_dict = {}
for l in range(len(list_of_participants)):
    names_dict[list_of_participants[l]] = {"Distance": 0}
while True:
    commands = input()
    if commands == "end of race":
        break
    matches = re.findall(pattern_name, commands)
    name = "".join(matches)
    if name in list_of_participants:
        match_digits = re.findall(pattern_digits, commands)
        digits = [int(x) for x in match_digits]
        digits = sum(digits)
        names_dict[name]["Distance"] += digits
    else:
        continue
sorted_dict = dict(sorted(names_dict.items(), key = lambda x: (x[1]["Distance"])))
result = []

for key, value in sorted_dict.items():
    result.append(key)
if len(result) >= 3:
    print(f"1st place: {result[-1]}")
    print(f"2nd place: {result[-2]}")
    print(f"3rd place: {result[-3]}")
else:
    print(f"1st place: {result[-1]}")
    print(f"2nd place: {result[-2]}")
    print(f"3rd place: ")

# George, Peter, Bill, Tom
# G4e@55or%6g6!68e!!@
# R1@!3a$y4456@
# B5@i@#123ll
# G@e54o$r6ge#
# 7P%et^#e5346r
# T$o553m&6
# end of race


