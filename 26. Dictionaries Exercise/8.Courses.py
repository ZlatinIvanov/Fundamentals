courses = {}
line = input()
while line != "end":
    course, name = line.split(" : ")
    if course not in courses:
        courses[course] = [name]
    else:
        courses[course] += [name]

    line = input()
for course in courses:
    print(f"{course}: {len(courses[course])}")
    for name in courses[course]:
        print(f"-- {''.join(name)}")