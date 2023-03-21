list_of_str_int = input().split()
number_for_removes = int(input())
new_list = []
for i in range(len(list_of_str_int)):
    list_of_str_int[i] = int(list_of_str_int[i])
for j in range(number_for_removes):
    min_number = min(list_of_str_int)
    list_of_str_int.remove(min_number)
for i in range(len(list_of_str_int)):
    list_of_str_int[i] = str(list_of_str_int[i])
print(', '.join(list_of_str_int))