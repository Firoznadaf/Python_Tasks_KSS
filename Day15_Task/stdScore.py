

import math
import os

# list of tuples
students = [
    ("Firoz", 85),
    ("Akshay", 45),
    ("Arun", 65),
    ("Kasim", 90),
    ("Kiran", 35)
]

#convert list into dictionary
student_dict = dict(students)

print("Student Details:", student_dict)

# find students scoring above 50
print("\nStudents scoring above 50:")

for name, marks in student_dict.items():
    if marks > 50:
        print(name, marks)

# calculate average
average = math.fsum(student_dict.values()) / len(student_dict)

print("\nAverage Marks:", average)

#The path of folder
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "student_results.txt")

# store result in a file
with open(file_path, "w") as file:
    file.write("Student Results\n")
    for name, marks in student_dict.items():
        file.write(f"{name}: {marks}\n")

    file.write(f"Average Marks: {average}")

print("\nResult saved successfully!")