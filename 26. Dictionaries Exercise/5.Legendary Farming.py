material_dict = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk_dict = {}
obtained = False
while not obtained:
    line = input()
    farming = line.split()
    for x in range(0, len(farming)-1, 2):
        quantity = int(farming[x])
        material = farming[x+1].lower()

        if material in material_dict:
            material_dict[material] += quantity
            if material_dict[material] >= 250:
                material_dict[material] -= 250
                obtained = True
                print(f"{legendary_item[material]} obtained!")
                break
        else:
            if material in junk_dict:
                junk_dict[material] += quantity
            else:
                junk_dict[material] = quantity

for material, quantity in material_dict.items():
    print(f"{material}: {quantity}")
for material, quantity in junk_dict.items():
    print(f"{material}: {quantity}")

