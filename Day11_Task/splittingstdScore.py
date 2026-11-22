# Splitting Student Scores Across Servers 

import numpy as np

scores = np.array([50, 60, 70, 80, 90, 100, 110, 120])

parts = np.array_split(scores, 4)

for part in parts:
    print(part)