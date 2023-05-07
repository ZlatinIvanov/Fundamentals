pirates = {}
flag = True
while True:
    commands = input()
    if commands == "Sail":
        break
    commands = commands.split("||")
    city = commands[0]
    population = int(commands[1])
    gold = int(commands[2])
    if city not in pirates:
        pirates[city] = {"Population": population, "Gold": gold}
    else:
        pirates[city]["Population"] += population
        pirates[city]["Gold"] += gold
while True:
    events = input()
    if events == "End":
        break
    events = events.split("=>")
    action = events[0]
    if action == "Plunder":
        city = events[1]
        population = int(events[2])
        gold = int(events[3])
        pirates[city]["Population"] -= population
        pirates[city]["Gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
        if pirates[city]["Gold"] <= 0 or pirates[city]["Population"] <= 0:
            print(f"{city} has been wiped off the map!")
            del pirates[city]
    if action == "Prosper":
        city = events[1]
        gold = int(events[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            pirates[city]["Gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {pirates[city]['Gold']} gold.")
    if not pirates:
        flag = False
        break
if flag:
    print(f"Ahoy, Captain! There are {len(pirates)} wealthy settlements to go to:")
    for city, value in pirates.items():
        people = value["Population"]
        gold = value["Gold"]
        print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

# Tortuga||345000||1250
# Santo Domingo||240000||630
# Havana||410000||1100
# Sail
# Plunder=>Tortuga=>75000=>380
# Prosper=>Santo Domingo=>180
# End
