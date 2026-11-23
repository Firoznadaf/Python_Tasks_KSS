# Random Sales Simulation 

import numpy as np

sales = np.random.randint(100, 501, 10)

print("Daily Sales:", sales)

average = np.mean(sales)

print("Avearge Sales:", average)