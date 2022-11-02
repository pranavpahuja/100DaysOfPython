student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
student_grades = {}
for key in student_scores.keys():
    marks = student_scores[key]
    if marks > 90 and marks <= 100:
        student_grades[key] = "Outstanding"
    elif marks > 80 and marks <= 90:
        student_grades[key] = "Exceeds Expectation"
    elif marks > 70 and marks <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)