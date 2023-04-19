rows = int(input())
students = {}

for n in range(rows):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)
for student, grade in students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade < 4.5:
        continue
    print(f"{student} -> {average_grade:.2f}")

