single_string = input()
emotions = ""
for char in range(len(single_string)):
    if single_string[char] == ":":
        emotions += single_string[char +1]
for emotion in emotions:
    print(f":{emotion}")
