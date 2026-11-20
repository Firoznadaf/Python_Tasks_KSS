# Splitting Data for Parallel Processing 

import numpy as np

data = np.array([5, 10, 15, 20, 25, 30])

parts = np.split(data, 3)

print("Split Arrays:")
for part in parts:
    print(part)