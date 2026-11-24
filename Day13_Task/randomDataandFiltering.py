# Random Data & Filtering

import numpy as np

nums = np.random.randint(1, 100, 10)

filtered = nums[nums % 5 == 0]

result = np.sort(filtered)

print("Random numbers:", nums)
print("Sorted multiples of 5:", result)