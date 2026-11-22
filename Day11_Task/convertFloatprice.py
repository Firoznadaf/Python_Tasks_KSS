# Convert Float Prices to Integer 

import numpy as np

prices = np.array([10.5, 20.8, 15.3])

new_prices = prices.astype(int)

print("Original array:", prices)
print("Integer array:", new_prices)