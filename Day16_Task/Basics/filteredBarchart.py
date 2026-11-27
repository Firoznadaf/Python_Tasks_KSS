

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

filtered_df = df[df["Marks"] > 50]

print(filtered_df)

plt.bar(filtered_df["Name"], filtered_df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Scoring Above 50")
plt.show()