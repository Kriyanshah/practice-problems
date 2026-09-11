students = {
    "Amit": 89,
    "kriyan": 98,
    "taksh": 8,
    "Abdul": 87,
    "alyssa": 69
}
highest_student = max(students, key=students.get)
print("Student with highest marks = ", highest_student)
print("Highest marks = ", students[highest_student])