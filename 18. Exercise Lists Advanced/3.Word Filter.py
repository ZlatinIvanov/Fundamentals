words_str = input().split()
for word in words_str:
    if len(word) % 2 == 0:
        print(word)