# Write a program to find the student with the highest marks from a dictionary. 

students = {
    "Firoz": 90,
    "Akshay": 85,
    "Kasim": 80
}

highest = max(students, key=students.get)

print("Student with highest marks:", highest)
print("Highest marks:", students[highest])