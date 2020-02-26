import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100)

fig = plt.figure(10)
fig.clf()

ax = fig.add_subplot(2, 2, 1)
ax.hist(x, histtype = 'bar', rwidth = 0.9)

ax2 = fig.add_subplot(2, 2, 2)
ax2.boxplot(x)
ax2.plot(np.zeros(100) + 1.2, x, '.')

plt.show()