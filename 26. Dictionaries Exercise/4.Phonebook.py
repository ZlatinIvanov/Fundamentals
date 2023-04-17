data = input()
phone_book = {}

while "-" in data:
    name, number = data.split("-")
    phone_book[name] = number
    data = input()
data = int(data)
for x in range(data):
    searched_name = input()
    if searched_name in phone_book:
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
