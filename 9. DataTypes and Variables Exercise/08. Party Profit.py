group_size = int(input())
days = int(input())

coins_per_day = 0
food_expenses = 0
drink_expenses = 0
gain_coins = 0
for d in range(1, days+1):
    if d % 15 == 0:
        group_size += 5
    if d % 10 == 0:
        group_size -= 2
    if d % 3 == 0:
        drink_expenses += 3 * group_size
    if d % 5 == 0:
        gain_coins += 20 * group_size
        if d % 3 == 0:
            drink_expenses += 2 * group_size
    coins_per_day += 50
    food_expenses += 2 * group_size
coins_per_companion = int((coins_per_day + gain_coins - drink_expenses - food_expenses) / group_size)
print(f"{group_size} companions received {coins_per_companion} coins each.")



