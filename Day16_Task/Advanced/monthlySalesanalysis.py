# Monthly Sales Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create data
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Slaes": sales
})

print(df)

# line graph
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# bar chart
plt.bar(months, sales)
plt.title("Month wise sales comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# pie chart
plt.pie(sales, labels=months, autopct="%1.1f%%")
plt.title("Monthly sales contribution")
plt.show()

# histogram
plt.hist(sales, bins=5, edgecolor='black')
plt.title("Frequency of sales values")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# scatter plot
plt.scatter(range(len(sales)), sales)
plt.title("Month index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.show()
