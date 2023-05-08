import re

text_string = input()
food_list = []
date_list = []
calories_list = []
pattern = r"(#|\|)([A-Za-z][\sA-Za-z]+)\1(\b\d{2}/\d{2}/\d{2})\1(\d{1,})\1"

matches = re.finditer(pattern, text_string)
total_calories = 0
for data in matches:
    food = data[2]
    date = data[3]
    calories = int(data[4])
    food_list.append(food)
    date_list.append(date)
    calories_list.append(calories)
    total_calories += calories
print(f"You have food to last you for: {total_calories // 2000} days!")
for x in range(len(food_list)):
    print(f"Item: {food_list[x]}, Best before: {date_list[x]}, Nutrition: {calories_list[x]}")



