# Student Marks DataFrame Analysis 

import pandas as pd

data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

# add total column
data["Total"] = data["Math"] + data["Science"]

print(data)

# find std with highest marks
topper = data.loc[data["Total"].idxmax()]

print("\nTopper:")
print(topper)