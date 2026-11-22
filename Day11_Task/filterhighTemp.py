# Filter High Temperature Values 

import numpy as np

temperature = np.array([28, 31, 35, 27, 40, 22])

result = temperature[temperature > 30]

print(result)