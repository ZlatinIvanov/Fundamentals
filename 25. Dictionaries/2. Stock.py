line = input().split(" ")
bakery = {}
for i in range(0, len(line), 2):
    key = line[i]
    value = line[i+1]
    bakery[key] = int(value)
searched_products = input().split(" ")
for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
