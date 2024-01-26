number_of_students = int(input())
students = {}
for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    average_grade = f"{sum(grades) / len(grades):.2f}"
    formatted_grades = f"{' '.join([f'{z:.2f}' for z in grades])}"
    print(f"{student} -> {formatted_grades} (avg: {average_grade})")
