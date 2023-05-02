import re

pattern = r">>([A-z]+)<<(\d+(\.\d+)?)\!(\d+)"
new_list = []
total_sum = 0
while True:
    line = input()
    if line == "Purchase":
        break
    matches = re.findall(pattern, line)
    if not matches:
        continue
    for match in matches:
        item = match[0]
        price = float(match[1])
        quantity = int(match[3])
        new_list.append(item)
        total_sum += price * quantity

print(f"Bought furniture:")
for n in new_list:
    print(f"{n}")
print(f"Total money spend: {total_sum:.2f}")
