# 14장 넘파이

"""
# Lab: BMI 계산하기
import numpy as np

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
weights = [86, 74, 59, 95, 80, 68]

heights = np.array(heights)
weights = np.array(weights)

bmi = weights / (heights**2)

print(bmi)

# Lab: 잡음이 들어간 직선 그리기

import matplotlib.pyplot as plt
import numpy as np

purse = np.linspace(1, 10, 100)
noise = np.random.rand(100)

signal = purse + noise

plt.plot(signal)
plt.show()

# Lab: 정규 분포 그래프 그리기
import numpy as np
import matplotlib.pyplot as plt

m, sigma = 10, 2

numbers1 = np.random.randn(10000)
numbers2 = m + sigma * np.random.randn(10000)

plt.hist(numbers1, bins=20)
plt.hist(numbers2, bins=20)
plt.show()

# Lab: sin함수 그리기

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = 3 * np.sin(x)

plt.plot(x, y1, x, y2)
plt.show()

#Lab: MSE 오차 계산하기
import numpy as np

ypred = np.array([1,0,0,0,0])
y=np.array([0,1,0,0,0])

#MSE = (1/len(ypred))*sum((ypred-y)**2)
MSE = np.mean((ypred-y)**2)

print(MSE)
"""

#Lab: 직원들의 월급 인상하기

#Lab: 그래프 그리기


