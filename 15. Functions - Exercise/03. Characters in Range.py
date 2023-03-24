def char_to_int(start, end):
    char_list = []
    start = ord(start)
    end = ord(end)
    for ch in range(start+1, end):
        char_list.append(chr(ch))
    return char_list


char_one = input()
char_two = input()
result = char_to_int(char_one, char_two)
print(' '.join(result))