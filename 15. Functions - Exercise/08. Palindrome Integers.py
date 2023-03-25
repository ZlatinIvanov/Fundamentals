# def palindrome(numbers):
#     for num in numbers:
#         if str(num) == str(num)[::-1]:
#             print(True)
#         else:
#             print(False)
#     return
#
#
# list_of_int = [int(x) for x in input().split(", ")]
#
# print(palindrome(list_of_int))

def is_palindrome(numbers):
    for num in numbers:
        if str(num) == str(num)[::-1]:
            print(True)
        else:
            print(False)


numbers = [int(x) for x in input().split(", ")]
is_palindrome(numbers)