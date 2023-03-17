people_n = int(input())
people_p = int(input())
remaining = people_n
result = 0
while True:
    if remaining > 0:
        remaining -= people_p
    else:
        break
    result += 1
print(result)