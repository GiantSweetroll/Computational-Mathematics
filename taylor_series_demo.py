import sympy as sp


x = sp.Symbol('x');
ori = (sp.sin(x))**3
ori1 = sp.sin(x).evalf(subs={x: 0.1})**3
print("Original:")
print(ori)
print(ori1)
print()

diff = sp.diff((sp.sin(x))**3)
diff1 = diff.evalf(subs={x: 0.1})
print("First derivative:")
print(diff)
print(diff1)
print()

print("Second derivative:")
diff = sp.diff(diff)
diff2 = diff.evalf(subs={x: 0.1})
print(diff)
print(diff2)
print()

print("Final Answer:")
answer = ori1 + diff1*(1.4) + (diff2*((1.4)**2))/2
print(answer)