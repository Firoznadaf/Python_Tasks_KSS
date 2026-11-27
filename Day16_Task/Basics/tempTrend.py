# Temperature Trend Line Plot 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

s = pd.Series(temps)

print(s)

plt.plot(s, marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()