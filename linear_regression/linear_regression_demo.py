import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

x = np.array([0.0, 1.0, 2.0, 2.5, 3.0])
y = np.array([2.9, 3.7, 4.1, 4.4, 5.0])

beta1 = y.dot(x - x.mean()) / (x.dot(x - x.mean()))
beta0 = y.mean() - beta1 * x.mean()

print(beta1)
print(beta0)

yHat = lambda x: beta0 + beta1*x

fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111)
ax.plot(x, y, 'o', label="data")
ax.plot(x, yHat(x), '-', label="model")
ax.legend()

plt.show()

#THE SECOND APPROACH TO GET MODEL COEFFICIENT
#A BETTER WAY
n = x.size
A = np.ones((n, 2))
A[:,1] = x
beta_model = np.linalg.lstsq(A, y)
beta_model2 = np.linalg.solve(A.transpose().dot(A), A.transpose().dot(y))   #Using gauss elimination
print(beta_model[0])
print(beta_model2)