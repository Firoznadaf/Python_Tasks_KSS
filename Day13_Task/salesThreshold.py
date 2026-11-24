# Sales Threshold Filtering

import numpy as np

sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])

avg = np.mean(sales)

result = sales[sales > avg]

print("Average sales:", avg)
print("Sales above average:", result)