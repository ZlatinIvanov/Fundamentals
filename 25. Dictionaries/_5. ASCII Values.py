symbols = input().split(", ")
dict = {}
for x in symbols:
    if x not in dict:
        dict[x] = ord(x)
    else:
        continue
print(dict)