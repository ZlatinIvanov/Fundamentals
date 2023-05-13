heroes = {}

while True:
    commands = input()
    if commands == "End":
        break
    commands = commands.split()
    command = commands[0]
    hero_name = commands[1]
    if command == "Enroll":
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []
    if command == "Learn":
        spell_name = commands[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name].append(spell_name)
    if command == "Unlear":
        pass