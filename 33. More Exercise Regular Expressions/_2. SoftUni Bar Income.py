import re

pattern = r"%([A-Z][a-z]+)%<([A-Za-z_0-9]+)>\|(\d)\|(\d[\.\d]*)\$"
total_income = 0
while True:
    commands = input()
    if commands == "end of shift":
        break
    matches = re.findall(pattern, commands)
    for match in matches:
        name = match[0]
        product = match[1]
        count = int(match[2])
        price = float(match[3])
        total_price = count * price
        print(f"{name}: {product} - {total_price:.2f}")
        total_income += total_price
print(f"Total income: {total_income:.2f}")
# %George%<Croissant>|2|10.3$
# %Peter%<Gum>|1|1.3$
# %Maria%<Cola>|1|2.4$
# end of shift
