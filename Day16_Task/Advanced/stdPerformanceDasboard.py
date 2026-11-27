# Student Performance Dashboard

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create data
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# create DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)

# line graph
plt.plot(students, marks, marker='o')
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.bar(students, marks)
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# pie chart
plt.pie([sum(marks > 50), sum(marks <= 50)],
        labels=["Pass", "Fail"], autopct="%1.1f%%")
plt.show()

# histogram
plt.hist(marks, bins=5, edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# scatter plot
plt.scatter(range(len(marks)), marks)
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()