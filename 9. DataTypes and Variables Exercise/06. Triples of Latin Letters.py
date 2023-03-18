numbers = int(input())

for i in range(0, numbers):
    for j in range(0, numbers):
        for k in range(0, numbers):
            print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")