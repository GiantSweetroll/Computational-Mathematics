import sympy as sp
from final_exam.numerical_diff import *

x = sp.Symbol('x')
f = sp.E**(-x)
x0 = 1

print(cd(f, x, x0))
print(bd(f, x, x0))
print(fd(f, x, x0))
print()
print(cd2(f, x, x0))
print(bd2(f, x, x0))
print(fd2(f, x, x0))