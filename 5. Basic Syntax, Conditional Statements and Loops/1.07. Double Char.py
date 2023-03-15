
while True:
    word = input()
    if word == "End":
        break
    new_word = ""
    for w in range(len(word)):
        new_word += word[w] + word[w]
    if word == "SoftUni":
        continue
    else:
        print(new_word)
