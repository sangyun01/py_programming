# 14장 넘파이

import numpy as np
import matplotlib.pyplot as plt


heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
weights = [86, 74, 59, 95, 80, 68]

heights = np.array(heights)
weights = np.array(weights)

bmi = weights / (heights**2)

print(bmi)
