import numpy as np
import matplotlib.pyplot as plt

durations = np.random.uniform(447, 521+1, 1000)

mean = np.mean(durations)
sd = np.std(durations)

print(durations)
#A
print("Mean:", mean)
print("Standard Deviation:", sd)

#B
range = 521-447
height = 1/range
range1 = 480-447
range2 = 521-500
probability = range1*height - range2*height
print("Probability:", probability)

#C
n_bins = 10
plt.hist(durations, n_bins, facecolor='blue', alpha=0.5)
plt.show()