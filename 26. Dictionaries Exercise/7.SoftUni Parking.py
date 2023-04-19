num_of_commands = int(input())
users = {}

for n in range(num_of_commands):
    command = input().split()
    if command[0] == "register":
        if command[1] in users:
            print(f"ERROR: already registered with plate number {command[2]}")
        else:
            users[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
    if command[0] == "unregister":
        if command[1] not in users:
            print(f"ERROR: user {command[1]} not found")
        else:
            print(f"{command[1]} unregistered successfully")
            users.pop(command[1])
for name, licence in users.items():
    print(f"{name} => {licence}")
