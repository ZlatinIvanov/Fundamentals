fire_cells = input().split("#")
water = int(input())
processed_cells = []
total_fire = 0
for cell in fire_cells:
    cell_arg = cell.split(" = ")
    type_of_fire = cell_arg[0]
    value_of_cell = int(cell_arg[1])

    if type_of_fire == "High" and (value_of_cell < 81 or value_of_cell > 125):
        continue
    if type_of_fire == "Medium" and (value_of_cell < 51 or value_of_cell > 80):
        continue
    if type_of_fire == "Low" and (value_of_cell < 1 or value_of_cell > 50):
        continue
    if value_of_cell > water:
        continue
    water -= value_of_cell
    processed_cells.append(value_of_cell)
    total_fire += value_of_cell
print("Cells:")
for cell in processed_cells:
    print(f" - {cell}")
effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")