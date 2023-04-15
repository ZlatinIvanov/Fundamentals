words = input().lower()
words = words.split()
dict = {}
for x in words:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1
for word, value in dict.items():
    if value % 2 != 0:
        print(word, end=" ")