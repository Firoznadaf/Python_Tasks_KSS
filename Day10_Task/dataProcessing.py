# Data Processing Pipeline 

import numpy as np

data = [12, 7, 25, 3, 18, 10]

arr = np.array(data)

sorted_arr = np.sort(arr)

parts =np.split(sorted_arr, 2)

sum1 = np.sum(parts[0])
sum2 = np.sum(parts[1])

print("First Split:", parts[0])
print("Second Split:", parts[1])

print("Sum of First Parts:", sum1)
print("Sum of Second Parts:", sum2)