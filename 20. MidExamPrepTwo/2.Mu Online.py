init_health = 100
init_bitcoins = 0
dungeon_rooms = input().split("|")
room = 0
is_valid = True
for x in dungeon_rooms:
    command, number = x.split()
    number = int(number)
    room += 1
    if command == "potion":
        if init_health + number > 100:
            healing = 100 - init_health
            init_health = 100
        else:
            init_health += number
            healing = number
        print(f"You healed for {healing} hp.")
        print(f"Current health: {init_health} hp.")
    elif command == "chest":
        init_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        init_health -= number
        if init_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            is_valid = False
            break

if is_valid:
    print("You've made it!")
    print(f"Bitcoins: {init_bitcoins}")
    print(f"Health: {init_health}")
