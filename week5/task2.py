import json

input_file = "students.json"
output_file = "students_with_averages.json"

with open(input_file, "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    student["average_grade"] = round(sum(grades) / len(grades))

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=2)

print("Averages calculated.")

