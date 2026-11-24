# Data Alignment Issue in Series Addition 

import pandas as pd

S1 = pd.Series(
    [10, 20, 30],
    index=["a", "b", "c"]
)

S2 = pd.Series(
    [5, 15, 25],
    index=["b", "c", "d"]
)

# add both series
result = S1 + S2

print("Original addition:")
print(result)

# replace NaN with 0
final_result = result.fillna(0)

print("\nAfter replacing NaN with 0:")
print(final_result)

# calculate total
print("\nFinal total:", final_result.sum())