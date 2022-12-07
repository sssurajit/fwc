import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#given data
A = np.array([-3,1])
C = np.array([1,1])

#direction vectors
d = A-C
m = np.array([7,-4]) #for given line

#angles
x1 = m.T@d
x2 = LA.norm(m)
x3 = LA.norm(d)
theta = np.arccos(x1/(x2*x3))

#Rotation matrix
def P(alpha):
    return np.array([np.cos(alpha),-np.sin(alpha),np.sin(alpha),np.cos(alpha)]).reshape(2,2)

#other vertices
B = P(-theta)@(C-A)*np.cos(theta) + A
D = P((np.pi/2)-theta)@(C-A)*np.sin(theta) + A
print('B = ',B)
print('D = ',D)

#plotting the rectangle
plt.axline(A,B)
plt.axline(B,C)
plt.axline(C,D)
plt.axline(A,D)

plt.grid('equal')
plt.axis('auto')
plt.show()
