num_of_lines = int(input())
tank_capacity = 255
liters_overall = 0
leftover = 0
liters_to_fit_in_tank = 0
for n in range(num_of_lines):
    liters_of_water = int(input())
    liters_overall += liters_of_water
    liters_to_fit_in_tank += liters_of_water
    if liters_to_fit_in_tank > tank_capacity:
        leftover += liters_of_water
        liters_to_fit_in_tank -= liters_of_water
        print("Insufficient capacity!")
print(liters_to_fit_in_tank)