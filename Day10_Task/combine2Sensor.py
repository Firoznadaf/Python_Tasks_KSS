# Combine Two Sensor Readings 

import numpy as np

sensor1 = np.array([10, 20, 30])
sensor2 = np.array([40, 50, 60])

combined = np.concatenated((sensor1, sensor2))

print("Combined Array:", combined)