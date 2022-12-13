from sympy import *
import numpy as np

x,y,a,b = symbols('x y a b')

#defining given hyperbola
v = np.array([[b**2,0],[0,-a**2]])
p = np.array([a*sec(x),b*tan(x)])
q = np.array([a*csc(x),b*cot(x)])
omat = np.array([[0,1],[-1,0]]) 

#transforming to sympy variables
V = Matrix(v)
Rot = Matrix(omat)
P = Matrix(p)
Q = Matrix(q)

#calculation
m1 = Rot*V*P
m2 = Rot*V*Q
m = Matrix([[m1.T],[m2.T]])
M = m.inv()
n = Matrix([m1.T*P,m2.T*Q])
R = M*n
print(simplify(R)[1]) # k value
