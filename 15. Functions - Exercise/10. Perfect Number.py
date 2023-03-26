def is_perfect_number(number):
    divisors = [x for x in range(1, number) if number % x == 0]
    if sum(divisors) == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


the_perfect_number = int(input())

is_perfect_number(the_perfect_number)