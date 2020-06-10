import sympy as sp
import matplotlib.pyplot as plt

xy_values = []

#Initialize x and y values (make sure the X values are in order)
xy_values.append([0, 0])
xy_values.append([10, 227.04])
xy_values.append([15, 362.78])
xy_values.append([20, 517.35])
xy_values.append([22.5, 602.97])

#Initialize divided difference table
table = []

for _ in range(len(xy_values)):
    temp = []
    for _ in range(len(xy_values) + 1):
        temp.append(-1)
    table.append(temp)
        
#Insert x and y values to table
for i in range(len(xy_values)):
    table[i][0] = xy_values[i][0]
    table[i][1] = xy_values[i][1]

#Do the divided difference table
y_bound = 1
for col in range(2, len(table[0])):
    for row in range(y_bound, len(table)):
        try:
            delta = (table[row][col-1] - table[y_bound-1][col-1]) / (table[row][0] - table[y_bound-1][0])
        except:
            delta = 0
        #print(table[row][col-1], '-', table[y_bound-1][col-1], "divide", table[row][0], '-', table[y_bound-1][0], '=', delta)
        table[row][col] = delta
    y_bound += 1

#Get an values
an = []
col = 1
for row in range(0, len(table)):
    an.append(table[row][col])
    col += 1
    
#create function and simplify it
x = sp.Symbol('x')
func = 0
for a in range(len(an)):
    product = an[a]
    for i in range(a):
        product *= (x - xy_values[i][0])
    func += product

func = sp.simplify(func)
print(func)

#Plotting
#split n and y
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
    new_y_values.append(func.evalf(subs={x:i/100}))
    
plt.plot(x_values, y_values, 'o', label='data')
plt.plot(new_x_values, new_y_values, '-', label='equation')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")

plt.show()