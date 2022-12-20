from sympy import * 
t = Symbol('t')
x = Symbol('x')
m = integrate(sin(t)/(pi-t), (t, 0, x))
print(integrate(m, (x, 0, pi)))
