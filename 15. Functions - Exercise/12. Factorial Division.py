def factorial(a, b):
    y = 1
    j = 1
    for x in range(2, a + 1):
        y *= x
    for i in range(2, b + 1):
        j *= i
    result = y / j

    return result


num_one = int(input())
num_two = int(input())

print(f"{factorial(num_one, num_two):.2f}")
