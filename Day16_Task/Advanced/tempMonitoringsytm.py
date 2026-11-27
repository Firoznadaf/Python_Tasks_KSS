# Temperature Monitoring System 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# craete data
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# create DataFrame
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)

# line chart
plt.plot(days, temps, marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

# bar chart
plt.bar(days, temps)
plt.title("Day wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

# pie chart
high = np.sum(temps > 30)
low = np.sum(temps <= 30)

plt.pie([high, low],
        labels=["High Temperature", "Low Temperature"],
        autopct="%1.1f%%")
plt.title("High vs Low Temperature")
plt.show()

# histogram
plt.hist(temps, bins=5, edgecolor='black')
plt.title("Temperature Frequency")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

# scatter plot
plt.scatter(range(len(temps)), temps)
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature")
plt.show()
