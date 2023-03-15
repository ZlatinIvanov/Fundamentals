count_words = int(input())

for n in range(count_words):
    word = input()
    if "," in word or "." in word or "_" in word:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")