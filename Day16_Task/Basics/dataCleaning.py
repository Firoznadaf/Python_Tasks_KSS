# Data Cleaning + Visualization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

# convert into series
s = pd.Series(data)

# replace NaN with man
mean_value = s.mean()
s = s.fillna(mean_value)

print("Cleaned Data:")
print(s)

# calculate average
average = s.mean()

# filter values greater than average
filtered = s[s > average]

print("Values Above Average:")
print(filtered)

plt.figure(figsize=(10, 4))

# line graph
plt.subplot(1, 2, 1)
plt.plot(s, marker='o')
plt.title("Cleaned Data")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(True)

# bar chart
plt.subplot(1, 2, 2)
plt.bar(filtered.index, filtered.values)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Values")

plt.tight_layout()
plt.show()