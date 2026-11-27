# Product Sales & Profit Analysis 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# craete data
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# ceate DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print(df)

# line graph
plt.plot(products, sales, marker='o')
plt.title("Product Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# bar chart
plt.bar(products, sales)
plt.title("Product vs Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# pie chart
plt.pie(sales, labels=products, autopct="%1.1f%%")
plt.title("Product Sales Contribution")
plt.show()

# histogram
plt.hist(profit, bins=5, edgecolor='black')
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# scatter plot
plt.scatter(sales, profit)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()