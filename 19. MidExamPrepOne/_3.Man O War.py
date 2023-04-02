pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())
is_valid = True
while True:
    command = input().split()

    if command[0] == "Retire":
        is_valid = False
        break
    if command[0] == "Fire":
        pass
    if command[0] == "Defend":
        pass
    if command[0] == "Repair":
        pass
    if command[0] == "Status":
        pass
if is_valid:
    pass

