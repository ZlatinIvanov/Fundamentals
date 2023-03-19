lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_counter = 0
sword_counter = 0
shield_counter = 0
armor_counter = 0
for n in range(1, lost_fights+1):
    if n % 2 == 0:
        helmet_counter += 1
    if n % 3 == 0:
        sword_counter += 1
    if n % 2 == 0 and n % 3 == 0:
        shield_counter += 1
    if n % 12 == 0:
    # if shield_counter % 2 == 0 and shield_counter != 0:
        armor_counter += 1
expenses = helmet_price * helmet_counter + sword_price * sword_counter + shield_price * shield_counter + armor_price * armor_counter
print(f"Gladiator expenses: {expenses:.2f} aureus")