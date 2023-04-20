side_by_player = {}
player_by_side = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break
    if " | " in line:
        args = line.split(" | ")
        side = args[0]
        user = args[1]
        if side not in player_by_side:
            player_by_side[side] = []
        if user not in side_by_player:
            side_by_player[user] = side
            player_by_side[side].append(user)
    else:
        args = line.split(" -> ")
        user = args[0]
        side = args[1]
        if side not in player_by_side:
            player_by_side[side] = []
        player_by_side[side].append(user)
        if user in side_by_player:
            old_side = side_by_player[user]
            player_by_side[old_side].remove(user)
            side_by_player[user] = side
        else:
            side_by_player[user] = side
        print(f"{user} joins the {side} side!")
for side, member in player_by_side.items():
    if len(member) == 0:
        continue
    print(f"Side: {side}, Members: {len(member)} ")
    for m in member:
        print(f"! {m}")

