# Remove Outliers

import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])

mean = np.mean(values)
std = np.std(values)

lower = mean - 2 * std
upper = mean + 2 * std

result = values[(values >= lower) & (values <= upper)]

print("Mean:", mean)
print("Standard deviation:", std)
print("After removing outliers:", result)