from math import ceil

seq_of_nums = [int(x) for x in input().split(", ")]
low = 1
high = 10

groups_count = ceil((max(seq_of_nums) / 10))

for x in range(1, groups_count +1):
    numbers = [x for x in seq_of_nums if low <= x <= high]
    print(f"Group of {10 * x}'s: {numbers}")

    low += 10
    high += 10
