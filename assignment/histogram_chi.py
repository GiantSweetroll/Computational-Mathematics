import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.random.chisquare(10, 1000)

fx, bin = np.histogram(x)
nbin = bin.size

fig = plt.figure(1); plt.clf();
ax = fig.add_subplot(1, 1, 1)
ax.bar(bin[0 : nbin-1], fx)

plt.show()