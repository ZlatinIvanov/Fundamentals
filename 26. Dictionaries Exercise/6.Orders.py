items_by_price = {}
items_by_quantity = {}
line = input()
while line != "buy":
    name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)
    items_by_price[name] = price
    if name not in items_by_quantity:
        items_by_quantity[name] = quantity
    else:
        items_by_quantity[name] += quantity
    line = input()
for item in items_by_price:
    price = items_by_price[item]
    quantity = items_by_quantity[item]
    total_price = price * quantity
    print(f"{item} -> {total_price:.2f}")
