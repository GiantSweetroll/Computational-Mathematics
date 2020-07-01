import sympy as sp;

def central_difference(f, x, xStart, h= 1.0E-4):
    df = (f.evalf(subs={x : xStart + h}) - f.evalf(subs={x : xStart - h}))/(2*h)
    return df;

def newton(f, xVal):
    while True:
        fx = f.evalf(subs={x : xVal})
        xVal = xVal -  fx/ central_difference(f, x, xVal)
        
        if abs(fx) < 1.0E-4:
            break
    
    return xVal

x = sp.Symbol('x')
function = x**2 - 2

print("Roots:", newton(function, 4))