def only_even_numbers(numbers):
    result = numbers % 2 == 0
    return result


sequence_of_numbers = [int(x) for x in input().split()]
print(list(filter(only_even_numbers, sequence_of_numbers)))
