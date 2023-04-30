import re
line = input()
match_list = []
pattern = r"\b_([A-Za-z0-9]*)\b"

matches = re.findall(pattern, line)

print(",".join(matches))