import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys
lib_path = '/home/jeet/iith/matrix/CoordGeo'
sys.path.insert(0,lib_path)

#local import
from line.funcs import *
from triangle.funcs import *

#if using termux
import subprocess
import shlex
#end if

# Coordinates of A and B
#A = np.array([1, -5])
#B = np.array([-4, 5])
# Calculate intersection
#x =(B - A)
#print(x)

#Point A and B
I = np.array([1,-5]) 
J = np.array([-4,5]) 
P = np.array([-1.5, 0])  

#Generating all lines
x_IJ = line_gen(I,J)

#Plotting all lines
plt.plot(x_IJ[0,:],x_IJ[1,:],color='green',label='$AB$')
plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 + 0.1), I[1] * (1 - 0.1) , 'A')
plt.plot(J[0], J[1], 'o')
plt.text(J[0] * (1 - 0.1), J[1] * (1) , 'B')

# Plotting point of k
plt.plot(P[0], P[1], marker='o',color='red', markersize=5)

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')


plt.xlabel('$ X $')
plt.ylabel('$ Y $')
plt.legend()
plt.grid(True) # minor
plt.axis('equal')
#if using termux                        
plt.savefig('/home/jeet/iith/vector/vector-2/figs/vec.pdf')                                           
subprocess.run(shlex.split("xdg-open /home/jeet/iith/vector/vector-2/figs/vec.pdf")) 
#plt.show()
