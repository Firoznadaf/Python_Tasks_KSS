# Random Matrix and Condition Filtering 

import numpy as np

arr = np.random.randint(0, 51, (3, 3))

print("Original Matrix:")
print(arr)

result = arr[arr > 25]

print("Values Greater Than 25:")
print(result)