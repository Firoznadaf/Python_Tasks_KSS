# Adding and Updating Columns

import pandas as pd

df = pd.DataFrame({
    "Price": [100, 200, 300]
})

# calculate discount
df["Discount"] = df["Price"] * 0.10

# calculate final price
df["Final Price"] = df["Price"] - df["Discount"]

print(df)