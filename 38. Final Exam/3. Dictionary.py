words_dict = {}
test_list = []
words_def = input().split(" | ")

for _ in words_def:
    word = _.split(": ")
    if word[0] not in words_dict:
        words_dict[word[0]] = [word[1]]

    else:
        words_dict[word[0]].append(word[1])
while True:
    commands = input()
    if commands == "Test":
        for j in test_list:
            if j in words_dict:
                print(f"{j}:")
                for k, value in words_dict.items():
                    if k == j:
                        for i in value:
                            print(f"-{i}")
        break
    if commands == "Hand Over":
        for y, value in words_dict.items():
            print(f"{y}", end=" ")
        break
    commands = commands.split(" | ")
    for x in commands:
        test_list.append(x)

# programmer: an animal, which turns coffee into code | developer: a magician
# fish | domino
# Hand Over
