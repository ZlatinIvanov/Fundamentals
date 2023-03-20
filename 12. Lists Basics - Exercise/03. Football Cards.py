card_sequence = input().split()
first_team_counter = 11
second_team_counter = 11
first_team_player = []
second_team_player = []
flag = False
for inx in card_sequence:
    if inx in first_team_player or inx in second_team_player:
        continue
    if "A" in inx:
        first_team_player.append(inx)
        first_team_counter -= 1
    if "B" in inx:
        second_team_player.append(inx)
        second_team_counter -= 1
    if first_team_counter < 7 or second_team_counter < 7:
        flag = True
        break
print(f"Team A - {first_team_counter}; Team B - {second_team_counter}")
if flag:
    print("Game was terminated")
