# Fruit Sales Comparison (Series Addition)

import pandas as pd

S1 = pd.Series(
    [10, 20, 30],
    index = ["apple", "banana", "cherry"]
)

S2 = pd.Series(
    [5, 15, 25],
    index=["apple", "banana", "cherry"]
)

# adding both series
result = S1 + S2

print("Fruit sales:")
print(result)

# total sale
print("Total sales:", result.sum())