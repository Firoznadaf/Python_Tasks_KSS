# Complex DataFrame Transformation 

import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

# calculate status column
df["Status"] = df["Marks"].apply(
    lambda x: "Fail" if x < 50 else "Pass"
)

print("Student Results:")
print(df)

# filter pass std
passed_students = df[df["Status"] == "Pass"]

print("\nPassed Students:")
print(passed_students)

# calculate average marks
average = passed_students["Marks"].mean()

print("\nAverage marks of passed students:", average)