#  Reshape & Row Averages 

import numpy as np

data = np.arange(1, 13)

matrix = data.reshape(3, 4)

averages = np.mean(matrix, axis=1)

print(matrix)
print("Row average:", averages)