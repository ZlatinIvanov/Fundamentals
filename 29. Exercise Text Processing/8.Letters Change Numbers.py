from string import ascii_lowercase

line = input().split()
total_sum = 0

for elem in line:
    number = int(elem[1:-1])
    first_letter = elem[0]
    last_letter = elem[-1]
    first_letter_alpha_position = ascii_lowercase.index(first_letter.lower()) + 1

    if first_letter.isupper():
        number /= first_letter_alpha_position
    else:
        number *= first_letter_alpha_position

    last_letter_alpha_position = ascii_lowercase.index(last_letter.lower()) + 1
    if last_letter.isupper():
        number -= last_letter_alpha_position
    else:
        number += last_letter_alpha_position
    total_sum += number
print(f"{total_sum:.2f}")
