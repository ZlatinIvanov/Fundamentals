numbers = int(input())
dict = {}
for _ in range(numbers):
    word = input()
    synonym = input()
    if word in dict:
        dict[word].append(synonym)
    else:
        dict[word] = [synonym]
for x, value in dict.items():
    print(f"{x} - {', '.join(value)}")

