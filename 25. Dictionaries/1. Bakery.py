line = input().split(" ")
bakery = {}
for i in range(0, len(line), 2):
    key = line[i]
    value = line[i+1]
    bakery[key] = int(value)

print(bakery)