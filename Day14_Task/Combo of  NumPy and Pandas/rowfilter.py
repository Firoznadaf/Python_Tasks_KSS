# Row Filtering + Aggregation 

import numpy as np
import pandas as pd

arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])

df = pd.DataFrame(arr, columns=["Sales", "Profit"])

print("Complete DataFrame:")
print(df)

filtered = df[df["Sales"] > 100]

print("\nFiltered DataFrame:")
print(filtered)

average_profit = filtered["Profit"].mean()

print("\nAverage Profit:", average_profit)