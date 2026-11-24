#  Temperature Alert System

import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])

result = np.where(temps > 30)

print(result)