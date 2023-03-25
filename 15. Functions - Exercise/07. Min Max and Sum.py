def min_max_sum(numbers):
    for n in numbers:
        minimun_number = min(numbers)
        maximum_number = max(numbers)
        sum_number = sum(numbers)

    return


num_str = [int(x) for x in input().split()]
print(f"The minimum number is {min(num_str)}")
print(f"The maximum number is {max(num_str)}")
print(f"The sum number is: {sum(num_str)}")
