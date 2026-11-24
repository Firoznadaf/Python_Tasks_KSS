#  Accessing Specific Data (Indexing) 

import pandas as pd

S = pd.Series(
    [100, 200, 300, 400],
    index=["A", "B", "C", "D"]
)

# access individual values
print("Value of B:", S["B"])
print("Value of D:", S["D"])

# access multiple values
result = S[["B", "D"]]
print("\nSubset:")
print(result)