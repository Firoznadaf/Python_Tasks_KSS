# Multi-Department Data Aggregation 

import numpy as np

branchA = np.array([10, 20],
                   [30, 40])

branchB = np.array([5, 15],
                   [25, 35])

combined = np.concatenate((branchA, branchB), axis=0)

total = np.sum(combined)

print("Combined Matrix:")
print(combined)

print("Total Employees:", total)
