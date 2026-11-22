# Reshape and Flatten Image Data 

import numpy as np

image = [[1, 2, 3],
         [4, 5, 6]]

arr = np.array(image)

flattened = arr.flatten()

print("Original array:")
print(arr)

print("Flattened array:")
print(flattened)