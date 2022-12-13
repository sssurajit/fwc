#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys
lib_path = '/sdcard/IITH/matrix/CoordGeo'
sys.path.insert(0,lib_path)

#local imports
from line.funcs import *
from triangle.funcs import *

#if using termux
import subprocess
import shlex
#end if

#Generating points on a standard hyperbola 
def hyper_gen(y, a, b):
    x = np.sqrt(1+(y**2)/(b**2))*a
    return x

# Function to generate tangent for hyberbola at P given array y
def tangent_gen(y, a, b, P):
    x = ((a**2)/P[0])*(1+(P[1]/(b**2))*y)
    return x

a = 2
b = 3
P = np.array([1*np.sqrt(0), 1.47])

I = np.array(([-4,0])) 
J = np.array(([4,2.9]))
K = np.array(([-4,2.9])) 
L = np.array(([4,0]))

x_IJ = line_gen(I,J)
x_KL = line_gen(K,L)

plt.plot(x_IJ[0,:],x_IJ[1,:],color='blue')
plt.plot(x_KL[0,:],x_KL[1,:],color='red')

# Plotting 4 sections of hyperbola individually
y = np.linspace(0.01,5,100)
x = hyper_gen(y, a, b)
plt.plot(x, y, color='green')

y = np.linspace(-5,-0.01,100)
x = hyper_gen(y, a, b)
plt.plot(x, y, color='green')

y = np.linspace(0.01,5,100)
x = -hyper_gen(y, a, b)
plt.plot(x, y, color='green')

y = np.linspace(-5,-0.01,100)
x = -hyper_gen(y, a, b)
plt.plot(x, y, color='green')

# Plotting point of k
plt.plot(P[0], P[1], marker='o', markersize=5)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')

plt.savefig('/sdcard/IITH/matrix/conic/fig.jpg')
plt.savefig('/sdcard/IITH/matrix/conic/fig.pdf')
subprocess.run(shlex.split("termux-open /sdcard/IITH/matrix/conic/fig.pdf"))
#plt.show()
