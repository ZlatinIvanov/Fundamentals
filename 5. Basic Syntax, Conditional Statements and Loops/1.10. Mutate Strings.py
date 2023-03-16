first_string = input()
second_string = input()

result = first_string
for i in range(len(first_string)):
    if first_string[i] == second_string[i]:
        continue
    result = second_string[:i+1] + first_string[i+1:]
    print(result)