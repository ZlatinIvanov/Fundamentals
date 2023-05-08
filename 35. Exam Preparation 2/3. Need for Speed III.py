nums_of_cars = int(input())
possession = {}
for n in range(nums_of_cars):
    cars = input().split("|")
    vehicle = cars[0]
    mileage = int(cars[1])
    gas = int(cars[2])
    possession[vehicle] = {"Mileage": mileage, "Fuel": gas}

while True:
    commands = input()
    if commands == "Stop":
        break
    commands = commands.split(" : ")
    command = commands[0]
    car = commands[1]
    if command == "Drive":
        distance = int(commands[2])
        fuel = int(commands[3])
        if possession[car]["Fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            possession[car]["Fuel"] -= fuel
            possession[car]["Mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if possession[car]["Mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del possession[car]
    if command == "Refuel":
        fuel = int(commands[2])
        fuel_filled = 75 - possession[car]["Fuel"]
        possession[car]["Fuel"] += fuel
        if possession[car]["Fuel"] > 75:
            possession[car]["Fuel"] = 75
            print(f"{car} refueled with {fuel_filled} liters")
        else:
            print(f"{car} refueled with {fuel} liters")
    if command == "Revert":
        kilometers = int(commands[2])
        possession[car]["Mileage"] -= kilometers
        if possession[car]["Mileage"] < 10000:
            possession[car]["Mileage"] = 10000
            continue
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for vehicle, value in possession.items():
    mileage = value["Mileage"]
    fuel = value["Fuel"]
    print(f"{vehicle} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
