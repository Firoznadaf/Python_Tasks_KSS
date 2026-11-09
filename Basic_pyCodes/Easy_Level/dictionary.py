# * Dictionary Operations: Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details.

students = {
    "Firoz": 85,
    "Akshay": 90,
    "Kasim": 78
}

# Add a new student
students["Farhan"] = 95

# Update existing student's marks
students["Firoz"] = 92

# Print all student details
for name, marks in students.items():
    print(name, ":", marks)
    