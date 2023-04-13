data = input()
courses = {}

while ":" in data:
    student_name, student_id, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {student_id: student_name}
    else:
        courses[course_name][student_id] = student_name
    data = input()
courses_name = data.replace("_", " ")
students = courses[courses_name]
for student_id, student_name in students.items():
    print(f"{student_name} - {student_id}")

# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals
