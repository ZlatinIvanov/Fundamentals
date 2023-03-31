line = [int(x) for x in input().split()]
magic_number = 0
total_sum = 0
while True:
    if not line:
        break
    for inx in line:
        number = int(input())
        magic_number = line[number]
        total_sum += magic_number
        if 0 <= number <= len(line):
            line.pop(number)
            for x in range(len(line)):
                if magic_number >= inx:
                    line[x] += magic_number
                else:
                    line[x] -= magic_number
        if number > len(line):
            for n in range(len(line)):
                if line[-1] >= line[n]:
                    line[n] += line[-1]
                else:
                    line[n] -= line[-1]
            line[-1] = line[0]
        if number < 0:
            for n in range(len(line)):
                if line[0] >= line[n]:
                    line[n] += line[0]
                else:
                    line[n] -= line[0]
            line[0] = line[-1]

print(total_sum)


