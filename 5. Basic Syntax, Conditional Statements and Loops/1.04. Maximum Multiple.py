divisor = int(input())
boundary = int(input())
base = 0
for n in range(0, boundary+1):
    if n % divisor == 0:
        base = n
print(base)