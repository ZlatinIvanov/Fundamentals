items_with_prices = input().split("|")
budget = float(input())
spending = 0
current_profit = 0
overall_profit = 0
bought_items = []
not_enough = False
for item in items_with_prices:
    item_arg = item.split("->")
    type_of_item = item_arg[0]
    price_of_item = float(item_arg[1])
    if type_of_item == "Clothes" and price_of_item > 50.00:
        continue
    if type_of_item == "Shoes" and price_of_item > 35.00:
        continue
    if type_of_item == "Accessories" and price_of_item > 20.50:
        continue
    if budget >= price_of_item:
        budget -= price_of_item
        current_profit = price_of_item * 0.4
        overall_profit += current_profit
        bought_items.append(price_of_item+current_profit)

for i in bought_items:
    print(f"{i:.2f} ", end="")
print()
print(f"Profit: {overall_profit:.2f}")
budget += sum(bought_items)
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")