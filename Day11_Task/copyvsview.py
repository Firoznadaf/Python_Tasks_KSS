# Copy vs View Behavior in Data Processing 

import numpy as np

arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy()

arr[0] = 100

print("Original array:", arr)
print("Copied array:", copy_arr)
