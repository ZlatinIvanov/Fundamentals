number_snowballs = int(input())
value_highest = 0
weight_highest = 0
time_best = 0
quality_best = 0

for n in range(1, number_snowballs+1):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())
    value = int((weight / time_to_target) ** quality)
    if value > value_highest:
        value_highest = value
        weight_highest = weight
        time_best = time_to_target
        quality_best = quality
print(f"{weight_highest} : {time_best} = {value_highest} ({quality_best})")