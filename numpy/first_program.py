import numpy as np

x = np.array([(1, 2), (4, 1)])  #Matrix dot matrix/vector is like matrix * matrix
y = np.array((1, 1))

z = np.dot(x, y)    #Statically
z = x.dot(y)        #By object method

print(z)

matrix = np.array((2, 4, 5, 6, 7, 9))

x = np.array([1, 2])
print(np.linalg.norm(x))        #Eucledean Norm

b = np.array([3, 7])

x = np.linalg.solve()