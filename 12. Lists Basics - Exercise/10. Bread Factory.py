init_energy = 100
init_coins = 100

events = input().split("|")

for e in events:
    e_arg = e.split("-")
    event_arg = e_arg[0]
    num_arg = int(e_arg[1])
    if event_arg == "rest":
        gained_energy = 0
        if num_arg + init_energy > 100:
            num_arg = 0
            print(f"You gained {num_arg} energy.")
            print(f"Current energy: {init_energy}.")
            continue
        else:
            init_energy += num_arg
            print(f"You gained {num_arg} energy.")
            print(f"Current energy: {init_energy}.")
    elif event_arg == "order":
        init_coins += num_arg
        init_energy -= 30
        if init_energy >= 0:
            print(f"You earned {num_arg} coins.")
        else:
            init_energy += 50
            print("You had to rest!")

    elif event_arg != "rest" and event_arg != "order":
        if init_coins >= num_arg:
            init_coins -= num_arg
            print(f"You bought {event_arg}.")
        else:
            print(f"Closed! Cannot afford {event_arg}.")
    else:
        pass
    # print(f"Day completed!")
    # print(f"Coins: {init_coins}")
    # print(f"Energy: {init_energy}")
