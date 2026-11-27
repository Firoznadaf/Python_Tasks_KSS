# Employee Salary Insights 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create data
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# craete DataFrame
df = pd.DataFrame({
    "Deapartment": departments,
    "Salary": salaries
})

print(df)

# line graph
plt.plot(range(len(salaries)), salaries, marker='o')
plt.title("Employee Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()

# bar chart
plt.bar(departments, salaries)
plt.title("Department wise Salary Comparison")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

# pie chart
dept_counts = df["Deapartment"].value_counts()

plt.pie(dept_counts.values,
        labels=dept_counts.index,
        autopct="%1.1f%%")
plt.title("Department Distribution")
plt.show()

# histogram
plt.hist(salaries, bins=5, edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show() 

# scatter plot 
plt.scatter(range(len(salaries)), salaries)
plt.title("Employee Index vs Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()
