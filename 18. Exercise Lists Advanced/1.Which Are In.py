substrings = input().split(", ")
strings = input().split(", ")
new_list = []

for substr in substrings:
    for word in strings:
        found = substr in word
        if found:
            new_list.append(substr)
            break
print(new_list)