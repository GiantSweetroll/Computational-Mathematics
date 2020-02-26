import matplotlib.pyplot as plt
import numpy as np

print(dir(plt)) #lists the available methods

fig = plt.figure(1)
#Set style
print(plt.style.available)      #display available styles
plt.style.use('ggplot')

plt.clf() #To clean

#Adding subplots
ax1 = fig.add_subplot(2, 2, 1)       #length, width, index
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 1, 2)

#Plotting
x = np.linspace(0, 2*np.pi, 100)        #distributed within 100 points (data)
y = np.sin(x)
z = np.cos(x)

ax1.plot(x, y, '-o', label = 'sin(x)', markersize = 10)
ax1.plot(x, z, '--s', label = 'cos(x)')

#Set labels
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax1.legend(ncol = 2)    #Add legend

plt.show()

#Save to file
fig.tight_layout()  #Sometimes the components when saved in file is messed up, this helps to mitigate it (experiment with different settings other than this)
fig.savefig('figure.png')