factor = int(input())
count = int(input())

list = []
for inx in range(1,count+1):
    number = inx * factor
    list.append(number)
print(list)
