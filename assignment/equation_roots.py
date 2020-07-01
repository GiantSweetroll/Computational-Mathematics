import sympy as sp

x = sp.Symbol('x')
function = x**2 - 2

def bisection(f, xl, xr):
    fxl = f.evalf(subs={x : xl})
    xm = 0
    
    while True:
        xm = (xl + xr)/2
        fxl = f.evalf(subs={x : xl})
        fxm = f.evalf(subs={x : xm})
        if fxl * fxm < 0:
            xr = xm
        else:
            xl = xm
        
        if abs(fxm) < 10**(-4):
            break
    
    return xm

def newton(f, df, xVal):
    while True:
        fx = f.evalf(subs={x : xVal})
        xVal = xVal -  fx/ df.evalf(subs={x : xVal})
        
        if abs(fx) < 10**(-4):
            break
    
    return xVal

def secant(f, x1, x2):
    xNew = 0
    
    while True:
        fx1 = f.evalf(subs={x : x1})
        fx2 = f.evalf(subs={x : x2})
        denominator = fx2 - fx1
        if denominator != 0:
            xNew = x2 - ((x2-x1)/denominator) * fx2
            if abs(xNew - x2) < 10*(-4):
                break
            else:
                x1 = x2
                x2 = xNew
        else:
            break
    
    return xNew

print("Bisection:", bisection(function, 0, 4))
print("Newton:", newton(function, sp.diff(function), 4))
print("Secant:", secant(function, 0, 4))