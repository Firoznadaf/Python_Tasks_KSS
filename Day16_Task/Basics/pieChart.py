#  Pie Chart with Conditional Data

import numpy as np
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

pass_count = np.sum(scores > 50)
fail_count = np.sum(scores <= 50)

labels = ["Pass", "Fail"]
counts = [pass_count, fail_count]

print("Pass:", pass_count)
print("Fail:", fail_count)

plt.pie(counts, labels=labels, autopct='%1.1f%%')
plt.title("Pass vs Fail")
plt.show()