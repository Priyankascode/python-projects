# Program to find the highest score in a class

# Sample data: list of students with their scores
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 96},
    {"name": "Eve", "score": 88}
]

# Find the highest score
highest_score = max(student["score"] for student in students)

# Print the result
print(f"The highest score in the class is: {highest_score}")

# Optionally, find the student with the highest score
highest_student = max(students, key=lambda s: s["score"])
print(f"The student with the highest score is {highest_student['name']} with {highest_student['score']} points.")