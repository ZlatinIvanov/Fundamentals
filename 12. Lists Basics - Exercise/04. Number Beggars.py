string_of_integers = input().split(", ")
count_of_beggars = int(input())
beggars = [0] * count_of_beggars
helper = 0
for inx in range(len(string_of_integers)):
    beggar_inx = inx % count_of_beggars
    num = int(string_of_integers[inx])
    beggars[beggar_inx] += num
print(beggars)