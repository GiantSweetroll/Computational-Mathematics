import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([10, 21, 25, 37, 50])

fig = plt.figure(1);
plt.clf();
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, "-o")
ax2 = fig.add_axes([0.2, 0.6, 0.2, 0.2])    #Display additional axes that can overlap placed graph
ax2.plot(np.sin(x), np.cos(x))

plt.show()