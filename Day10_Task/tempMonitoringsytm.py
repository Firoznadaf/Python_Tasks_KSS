# Temperature Monitoring System 

import numpy as np

day1 = [30, 32, 31]
day2 = [29, 33, 34]

temp = np.array([day1, day2])

print("Temperature Array:")
print(temp)

print("Total Temperature:", np.sum(temp))