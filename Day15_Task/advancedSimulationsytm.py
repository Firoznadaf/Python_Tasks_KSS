

import random
import numpy as np
import pandas as pd
import math
import os

script_folder = os.path.dirname(os.path.abspath(__file__))
numbers_file = os.path.join(script_folder, "exam_report.txt")

# Student class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = ""

    def assign_grade(self):

        if self.marks >= 90:
            self.grade = "A"

        elif self.marks >= 75:
            self.grade = "B"

        elif self.marks >= 60:
            self.grade = "C"

        elif self.marks >= 40:
            self.grade = "D"

        else:
            self.grade = "Fail"


try:

    names = [
        "Firoz", "Akshay", "Kasim",
        "Yasin", "Kiran", "Amit",
        "Tony", "Mark", "Pooja", "John"
    ]

    # Generate random marks
    marks = np.array([
        random.randint(0, 100)
        for i in range(10)
    ])

    students = []

    # Create student objects
    for i in range(10):

        student = Student(names[i], int(marks[i]))

        student.assign_grade()

        students.append(student)

    # Display results
    print("EXAM RESULTS")

    for student in students:
        print(
            student.name,
            student.marks,
            student.grade
        )

    # Create DataFrame
    df = pd.DataFrame({
        "Name": [s.name for s in students],
        "Marks": [s.marks for s in students],
        "Grade": [s.grade for s in students]
    })

    print("\nStudent Report:")
    print(df)

    # Statistics using math module
    average = math.fsum(marks) / len(marks)

    highest = max(marks)
    lowest = min(marks)

    print("\nAverage Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

    # Save report
    with open(numbers_file, "w") as file:

        file.write("EXAM REPORT\n\n")

        file.write(df.to_string(index=False))

        file.write(f"\n\nAverage Marks: {average}")
        file.write(f"\nHighest Marks: {highest}")
        file.write(f"\nLowest Marks: {lowest}")

    print("\nReport saved successfully!")

except (ValueError, IOError) as e:
    print("Error:", e)