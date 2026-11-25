

import numpy as np
import pandas as pd

# generate random marks
marks = np.random.randint(0, 101, 10)

# create DataFrame
df = pd.DataFrame({
    "Student": [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J"
    ],
    "Marks": marks
})

print("Student Marks:")
print(df)

# filter passing students
passed = df[df["Marks"] >= 40]

print("\nPassing Students:")
print(passed)

# calculate mean
average = np.mean(marks)

print("\nAverage Marks:", average)

# print results using loop
print("\nStudent Results:")

for index, row in df.iterrows():
    if row["Marks"] >= 40:
        print(row["Student"], "- Pass")
    else:
        print(row["Student"], "- Fail")