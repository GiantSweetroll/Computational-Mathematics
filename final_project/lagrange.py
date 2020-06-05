import sympy as sp
from pandas._libs import index

xy_values = []

#Initialize x and y values (make sure the X values are in order)
xy_values.append([0, 0])
xy_values.append([10, 227.04])
xy_values.append([15, 362.78])
xy_values.append([20, 517.35])
xy_values.append([22.5, 602.97])
xy_values.append([30, 901.67])

#Order of polynomial
n = 1       #Linear

#Value of x to find
xVal = 16

#Select the two data points between the selected xVal
indexes = []
for i in range(len(xy_values)-1):
    if xy_values[i][0] < xVal and xy_values[i+1][0] > xVal:
        indexes.append(i)
        indexes.append(i+1)
        
#Find the weighting functions
t = sp.Symbol('t');
wFunc = []      #Collection of Ln(t)
for i in range(n+1):
    subFunc = []    #Collection of individual (t - tj)/(ti-tj)
    for j in range(n+1):
        #j != i
        if i != j:
            #(t - tj)/(ti-tj)
            #sub = [i, j]
            #sub[0] = ti
            #sub[1] = tj
            sub = []
            sub.append(i)
            sub.append(j)
            subFunc.append(sub)
    wFunc.append(subFunc)
    
#Add them Together
total = 0
for i in range(len(wFunc)):
    weight_function_prod = 1
    for a in range(len(wFunc[i])):
        iIndex = wFunc[i][a][0]
        print("iIndex=", iIndex)
        index = indexes[iIndex]
        print("index=", index)
        ti = xy_values[index][0]
        print("ti=", ti)
        jIndex = wFunc[i][a][1]
        print("jIndex=", jIndex)
        index = indexes[jIndex]
        print("index=", index)
        tj = xy_values[index][0]
        print("tj=", tj)
        print("operation= (", t,"-", tj,") / (", ti, "-", tj, ")")
        sub = (t - tj)/ (ti - tj)
        print("sub weight function=", sub)
        weight_function_prod *= sub
    #Multiply by f(i)
    print("weight_function_prod =", weight_function_prod)
    print("xy_values=", xy_values[indexes[i]][1])
    total += weight_function_prod * xy_values[indexes[i]][1]
    print("current total=", total)

print("total=", total)

#Solve with xVal
result = total.evalf(subs={t : xVal})
print("result =", result) 