def add_nums(a,b):
    add = a + b
    return add


def subtrack_nums(a,b):
    subtrack = a - b
    return subtrack


first = int(input())
second = int(input())
third = int(input())
result = subtrack_nums(add_nums(first,second),third)
print(result)