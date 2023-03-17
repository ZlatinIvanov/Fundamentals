number_of_lines = int(input())
result = ""
total_sum = 0

for n in range(number_of_lines):
    letter = input()
    letter_convert = ord(letter)
    total_sum += letter_convert

print(f"The sum equals: {total_sum}")