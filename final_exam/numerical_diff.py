def cd(f, x, xStart, h= 1.0E-4):
    """
    Get first derivative using central difference method.
    
    params:
    f - the function equation
    x - the Sympy Symbol object
    xStart - the starting value of x
    h - the step size
    
    returns the value of the first derivative at xStart.
    """
    df = (f.evalf(subs={x : xStart + h}) - f.evalf(subs={x : xStart - h}))/(2*h)
    return df;

def cd2(f, x, xStart, h= 1.0E-4):
    """
    Get second derivative using central difference method.
    
    params:
    f - the function equation
    x - the Sympy Symbol object
    xStart - the starting value of x
    h - the step size
    
    returns the value of the second derivative at xStart.
    """
    df = (f.evalf(subs={x : xStart + h}) - 2*f.evalf(subs={x : xStart}) + f.evalf(subs={x : xStart - h}))/(h**2)
    return df;

def bd(f, x, xStart, h= 1.0E-4):
    """
    Get first derivative using backward difference method.
    
    params:
    f - the function equation
    x - the Sympy Symbol object
    xStart - the starting value of x
    h - the step size
    
    returns the value of the first derivative at xStart.
    """
    df = (f.evalf(subs={x : xStart}) - f.evalf(subs={x : xStart - h}))/(h)
    return df

def bd2(f, x, xStart, h= 1.0E-4):
    """
    Get second derivative using backward difference method.
    
    params:
    f - the function equation
    x - the Sympy Symbol object
    xStart - the starting value of x
    h - the step size
    
    returns the value of the second derivative at xStart.
    """
    df = (f.evalf(subs={x : xStart}) - 2*f.evalf(subs={x : xStart - h}) + f.evalf(subs={x : xStart - 2*h}))/(h**2)
    return df;

def fd2(f, x, xStart, h= 1.0E-4):
    """
    Get second derivative using forward difference method.
    
    params:
    f - the function equation
    x - the Sympy Symbol object
    xStart - the starting value of x
    h - the step size
    
    returns the value of the second derivative at xStart.
    """
    df = (f.evalf(subs={x : xStart + 2*h}) - 2*f.evalf(subs={x : xStart + h}) + f.evalf(subs={x : xStart}))/(h**2)
    return df;

def fd(f, x, xStart, h= 1.0E-4):
    """
    Get first derivative using forward difference method.
    
    params:
    f - the function equation
    x - the Sympy Symbol object
    xStart - the starting value of x
    h - the step size
    
    returns the value of the first derivative at xStart.
    """
    df = (f.evalf(subs={x : xStart + h}) - f.evalf(subs={x : xStart}))/(h)
    return df