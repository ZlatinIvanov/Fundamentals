line_string = input().split()
new_list = []
while True:
    command = input().split()
    if command[0] == "3:1":
        break
    if command[0] == "merge":
        start_inx = int(command[1])
        end_inx = int(command[2]) + 1
        # for m in range(len(line_string)):
        new_list.append("".join(line_string[start_inx:end_inx]))
        del line_string[start_inx:end_inx]
        line_string.insert(start_inx, "".join(new_list))
        new_list.clear()
    if command[0] == "divide":
        inx = int(command[1])
        partition = int(command[2])
        element = line_string[inx]
        partition_length = len(element) // partition
        result = [element[i:i+partition_length] for i in range(0, len(element), partition_length)]
        if len(result) > partition:
            last_partition = result.pop()
            result[-1] += last_partition
        line_string.pop(inx)
        line_string[inx:inx] = result

print(" ".join(line_string))
