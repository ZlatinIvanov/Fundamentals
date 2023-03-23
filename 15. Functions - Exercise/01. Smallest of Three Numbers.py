def smallest_number(number):
    min_num = float('inf')
    for n in number:
        if n < min_num:
            min_num = n
    return min_num

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_number([first_num,second_num,third_num]))
