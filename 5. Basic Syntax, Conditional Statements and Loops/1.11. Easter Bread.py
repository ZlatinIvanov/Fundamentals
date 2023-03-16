budget = float(input())
flour_price_per_kilo = float(input())
pack_of_eggs_price = flour_price_per_kilo * 0.75
milk_price_per_liter = flour_price_per_kilo * 1.25
price_for_one_loaf = flour_price_per_kilo + pack_of_eggs_price + milk_price_per_liter * 0.25
spent_counter = 0
bread_counter = 0
easter_eggs_counter = 0
while True:
    spent_counter += price_for_one_loaf
    if budget < spent_counter:
        break
    bread_counter += 1
    easter_eggs_counter += 3
    if bread_counter % 3 == 0:
        easter_eggs_counter -= (bread_counter - 2)
money_left = (budget - spent_counter) + price_for_one_loaf
print(f"You made {bread_counter} loaves of Easter bread! Now you have {easter_eggs_counter} eggs and {money_left:.2f}BGN left.")


