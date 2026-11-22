# Accessing Matrix Data

import numpy as np

marks = [[78, 85],
         [90, 88],
         [67, 72]]

arr = np.array(marks)

print("Second student's second subject marks:", arr[1, 1])