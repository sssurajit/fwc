import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys
lib_path = '/sdcard/IITH/matrix/CoordGeo'
sys.path.insert(0,lib_path)
#local import
from line.funcs import *
#if using termux
import subprocess
import shlex
#end if

#1 Point A,B and C
I = np.array([7,-2]) 
J = np.array([5,1])   
K = np.array([3,4])
#1 Generating all lines
x_IJ = line_gen(I,J)
x_JK = line_gen(J,K)
x_KI = line_gen(K,I)

#1 Plotting all lines
plt.plot(x_IJ[0,:],x_IJ[1,:],color='gold',label='$ABC$')
plt.plot(x_JK[0,:],x_JK[1,:],color='gold')

#1 plotting the all point
plt.plot(I[0], I[1], 'o',color='b')
plt.text(I[0] * (1 + 0.1), I[1] * (1 - 0.1) , 'A(7,-2)')
plt.plot(J[0], J[1], 'o',color='b')
plt.text(J[0] * (1 - 0.1), J[1] * (1) , 'B(5,1)')
plt.plot(K[0], K[1], 'o',color='b')
plt.text(K[0] * (1 - 0.1), K[1] * (1) , 'C(3,4)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux                        
plt.savefig('/sdcard/IITH/vector/vector-3/figs/vec-1.pdf')                                           
subprocess.run(shlex.split("termux-open /sdcard/IITH/vector/vector-3/figs/vec-1.pdf")) 
#plt.show()
