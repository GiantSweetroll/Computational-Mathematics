import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

x = np.array([4.51, 3.58, 4.31, 5.06, 5.64, 4.99, 5.29, 5.83, 4.70, 5.61, 4.90, 4.20])
y = np.array([2.48, 2.26, 2.47, 2.77, 2.99, 3.05, 3.18, 3.46, 3.03, 3.26, 2.67, 2.53])

#Approach 1
beta1 = y.dot(x - x.mean()) / (x.dot(x - x.mean()))
beta0 = y.mean() - beta1 * x.mean()

#Calculate R2
correlation_matrix = np.corrcoef(x, y)
correlation_xy = correlation_matrix[0,1]
r2 = correlation_xy**2

yHat = lambda x: beta0 + beta1*x

fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111)
ax.plot(x, y, 'o', label="data")
ax.plot(x, yHat(x), '-', label="model")
ax.legend()

plt.legend(loc='best', frameon=False)

print("R^2 =", r2)
plt.show()