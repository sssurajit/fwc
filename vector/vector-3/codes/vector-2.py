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

#2 Point A,B and C
L = np.array([8,1]) 
M = np.array([3,-4])   
N = np.array([2,-5])
#2 Generating all lines
x_LM = line_gen(L,M)
x_MN = line_gen(M,N)
x_NL = line_gen(N,L)
#2 Plotting all lines
plt.plot(x_LM[0,:],x_LM[1,:],color='r',label='$ABC$')
plt.plot(x_MN[0,:],x_MN[1,:],color='r')
#2 plotting the all point
plt.plot(L[0], L[1], 'o',color='g')
plt.text(L[0] * (1 + 0.1), L[1] * (1 - 0.1) , 'A(8,1)')
plt.plot(M[0], M[1], 'o',color='g')
plt.text(M[0] * (1 - 0.1), M[1] * (1) , 'B(3,-4)')
plt.plot(N[0], N[1], 'o',color='g')
plt.text(N[0] * (1 - 0.1), N[1] * (1) , 'C2,-5')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux                        
plt.savefig('/sdcard/IITH/vector/vector-3/figs/vec-2.pdf')                                           
subprocess.run(shlex.split("termux-open /sdcard/IITH/vector/vector-3/figs/vec-2.pdf")) 
#plt.show()
