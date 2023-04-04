seq_of_elements = input().split()
moves = 0
is_valid = True
while True:
    integers = input().split()
    if integers[0] == "end":
        if len(seq_of_elements) > 0:
            print("Sorry you lose :(")
            print(" ".join(seq_of_elements))
        is_valid = False
        break
    else:
        first = int(integers[0])
        second = int(integers[1])
    moves += 1
    to_add = f"-{moves}a"
    # to_add = int(to_add)
    if seq_of_elements[first] != seq_of_elements[second]:
        if first < 0 or second < 0 or first and second > len(seq_of_elements) or first == second:
            seq_of_elements.insert(int(len(seq_of_elements)/2),  to_add)
            seq_of_elements.insert(int(len(seq_of_elements)/2),  to_add)
            print("Invalid input! Adding additional elements to the board")
        else:
            print("Try again!")
    if seq_of_elements[first] == seq_of_elements[second]:
        print(f"Congrats! You have found matching elements - {seq_of_elements[first]}!")
        seq_of_elements[first] = "element1"
        seq_of_elements[second] = "element2"
        seq_of_elements.remove("element1")
        seq_of_elements.remove("element2")
        if len(seq_of_elements) == 0:
            break

if is_valid:
    print(f"You have won in {moves} turns!")


