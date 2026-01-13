import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    student["average_grade"] = round(sum(grades) / len(grades), 2)

with open("students_with_averages.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=2)

print("Averages calculated.")

