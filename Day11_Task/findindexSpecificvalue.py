#  Find Indexes of Specific Value

import numpy as np

codes = np.array([2, 4, 1, 4, 3, 4, 5])

indexes = np.where(codes == 4)

print(indexes)