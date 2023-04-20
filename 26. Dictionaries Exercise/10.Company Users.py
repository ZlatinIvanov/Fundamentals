companies = {}
while True:
    command = input()
    if command == "End":
        break
    name, employee_id = command.split(" -> ")
    if name in companies:
        if employee_id in companies[name]:
            continue
        companies[name] += [employee_id]
    else:
        companies[name] = [employee_id]

for name in companies:
    print(name)
    for id in companies[name]:
        print(f"-- {id}")
