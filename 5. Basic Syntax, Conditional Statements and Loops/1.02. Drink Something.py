age = int(input())
drink_type = ""
if age <= 14:
    drink_type = "toddy"
elif 14 < age <= 18:
    drink_type = "coke"
elif 18 < age <= 21:
    drink_type = "beer"
else:
    drink_type = "whisky"
print(f"drink {drink_type}")
