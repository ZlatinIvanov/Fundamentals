from math import ceil


num_of_students = int(input())
num_of_lectures = int(input())
bonus = int(input())
total_bonus = 0
max_bonus = 0
attendances_max = 0
for _ in range(num_of_students):
    attendances = int(input())
    if attendances != 0:
        total_bonus = attendances / num_of_lectures * ( 5 + bonus)
        if max_bonus < total_bonus:
            max_bonus = total_bonus
            attendances_max = attendances
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attendances_max} lectures.")
