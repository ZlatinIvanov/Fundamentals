def digit_to_char(word):
    temp = ""

    for ch in word:
        if not str(ch).isdigit():
            break

        temp += ch
    ascii_value = int(temp)
    char_value = chr(ascii_value)
    new_word = word.replace(temp, char_value)
    return new_word

def replace_in_word(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]

    return "".join(temp)


def decrypt(word):
    res = digit_to_char(word)
    res = replace_in_word(res)
    return res


secret_message = input().split()
new_message = [decrypt(word) for word in secret_message]
print(" ".join(new_message))
