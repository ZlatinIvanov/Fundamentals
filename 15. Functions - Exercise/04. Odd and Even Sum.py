def sum_of_number_type(num):
    even_sum = 0
    odd_sum = 0
    for n in num:
        n = int(n)
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n

    return [even_sum, odd_sum]


number = input()
result = sum_of_number_type(number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
