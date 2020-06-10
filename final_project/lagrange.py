import sympy as sp
import matplotlib.pyplot as plt

xy_values = []

#Initialize x and y values (make sure the X values are in order)
xy_values.append([0, 0])
xy_values.append([10, 227.04])
xy_values.append([15, 362.78])
xy_values.append([20, 517.35])
xy_values.append([22.5, 602.97])
xy_values.append([30, 901.67])

#Select the two data points between the selected xVal
def get_first2_indexes(xy_values, xVal):
    indexes = []
    for i in range(len(xy_values)-1):
        if xy_values[i][0] < xVal and xy_values[i+1][0] > xVal:
            indexes.append(i)
            indexes.append(i+1) 
    return indexes

#Find the other data points when n>1
def get_remaining_indexes(xy_values, indexes, xVal, n):
    for _ in range(n-1):
        #find the value nearest to xVal
        leftIndex = indexes[0]-1
        rightIndex = indexes[len(indexes)-1] + 1
        #Check if the adjacent index exists in the given xy_values data
        if (leftIndex > -1):
            if (rightIndex < len(xy_values)):
                #Check which one is closer to xVal
                if (abs(xy_values[leftIndex][0] - xVal) < abs(xy_values[rightIndex][0] - xVal)):
                    indexes.insert(0, leftIndex)
                else:
                    indexes.append(rightIndex)
            else:
                indexes.insert(0, leftIndex)
        elif (rightIndex < len(xy_values)):
            indexes.append(rightIndex)
        
                
#Find the weighting functions
def gather_weighting_functions(polynomial):
    wFunc = []      #Collection of Ln(x)
    for i in range(polynomial+1):
        subFunc = []    #Collection of individual (x - xj)/(xi-xj)
        for j in range(polynomial+1):
            #j != i
            if i != j:
                #(x - xj)/(xi-xj)
                #sub = [i, j]
                #sub[0] = xi
                #sub[1] = xj
                sub = []
                sub.append(i)
                sub.append(j)
                subFunc.append(sub)
        wFunc.append(subFunc)
        
    return wFunc
    
#Add them Together
def get_equation(xy_values, wFunc, indexes, x_symbol):
    total = 0
    for i in range(len(wFunc)):
        weight_function_prod = 1
        for a in range(len(wFunc[i])):
            iIndex = wFunc[i][a][0]
#             print("iIndex=", iIndex)
            index = indexes[iIndex]
#             print("index=", index)
            ti = xy_values[index][0]
#             print("ti=", ti)
            jIndex = wFunc[i][a][1]
#             print("jIndex=", jIndex)
            index = indexes[jIndex]
#             print("index=", index)
            tj = xy_values[index][0]
#             print("tj=", tj)
#             print("operation= (", x_symbol,"-", tj,") / (", ti, "-", tj, ")")
            sub = (x_symbol - tj)/ (ti - tj)
#             print("sub weight function=", sub)
            weight_function_prod *= sub
        #Multiply by f(i)
#         print("weight_function_prod =", weight_function_prod)
#         print("xy_values=", xy_values[indexes[i]][1])
        total += weight_function_prod * xy_values[indexes[i]][1]
#         print("current total=", total)
    return sp.simplify(total)

#Solve with xVal
x = sp.Symbol('x');
n = 5       #Order of polynomial (Linear = 1)
xVal = 16 #Value of x to find
indexes = get_first2_indexes(xy_values, xVal)
get_remaining_indexes(xy_values, indexes, xVal, n)
wFunc = gather_weighting_functions(n)
equation = get_equation(xy_values, wFunc, indexes, x)
result = equation.evalf(subs={x : xVal})
print("result =", result) 

#Graphing
def graph_lagrange(xy_values, equation, xVal, result, x_symbol):
    #split x and y
    x_values = []
    y_values = []
    
    for i in range(len(xy_values)):
        x_values.append(xy_values[i][0])
        y_values.append(xy_values[i][1])
    
    #Generate x and y
    new_x_values = []
    new_y_values = []
    for i in range(int(min(x_values) * 100), int(max(x_values) * 100), 1):
        new_x_values.append(i/100)
        new_y_values.append(equation.evalf(subs={x_symbol:i/100}))
        
    plt.plot(x_values, y_values, 'o', label='data')
    plt.plot(new_x_values, new_y_values, '-', label='equation')
    plt.plot([xVal], [result], '+', label="interpolated data")
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    
    plt.show()

graph_lagrange(xy_values, equation, xVal, result, x)