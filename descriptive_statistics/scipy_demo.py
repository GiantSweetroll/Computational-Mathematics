import scipy as sp
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

data1 = sp.randn(100)   #generate 100 random number

print(sp.median(data1))
print(stats.describe(data1))
print(stats.skew(data1))

x = stats.uniform(0, 15)
x_samples = x.rvs(2000)

plt.hist(x_samples, density=1, bins=50)
plt.plot(x_samples, x.pdf(x_samples), lw=5)

plt.show()

print(x.mean())
print(x.std())

x = stats.norm(loc=0, scale=1)
x_samples = x.rvs(50000)

plt.hist(x_samples, density=1)
plt.plot(np.linspace(-3, 3, 1000), x.pdf(np.linspace(-3, 3, 1000)))

plt.show()