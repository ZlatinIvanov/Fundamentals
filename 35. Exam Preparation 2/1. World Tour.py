all_stops = input()

while True:
    commands = input()
    if commands == "Travel":
        break
    commands = commands.split(":")
    instruction = commands[0]
    if instruction == "Add Stop":
        inx = int(commands[1])
        destination = commands[2]
        if inx <= len(all_stops):
            all_stops = all_stops[:inx] + destination + all_stops[inx:]
        else:
            continue
    if instruction == "Remove Stop":
        start_inx = int(commands[1])
        end_inx = int(commands[2]) +1
        if start_inx <= end_inx and end_inx <= len(all_stops):
            all_stops = all_stops[:start_inx] + all_stops[end_inx:]
    if instruction == "Switch":
        old_string = commands[1]
        new_string = commands[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
    print(all_stops)
print(f"Ready for world tour! Planned stops: {all_stops}")
