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
L = np.array([2,-2]) 
M = np.array([3,7])   
N = np.array([1,2])
O = np.array([3,-2])
S = np.array([24/11,-4/11])
#2 Generating all lines
x_LM = line_gen(L,M)
x_NO = line_gen(N,O)
#2 Plotting all lines
plt.plot(x_LM[0,:],x_LM[1,:],color='orange',label='$AB$')
plt.plot(x_NO[0,:],x_NO[1,:],color='cyan',label='$Line$')
#2 plotting the all point
plt.plot(L[0], L[1], 'o',color='g')
plt.text(L[0] * (1 + 0.1), L[1] * (1 - 0.1) , 'A(2,-2)')
plt.plot(M[0], M[1], 'o',color='g')
plt.text(M[0] * (1 - 0.1), M[1] * (1) , 'B(3,7)')

#Point of intersection
plt.plot(S[0], S[1], marker='o',color='red')
plt.text(S[0] * (1 - 0.1), S[1] * (1) , 'P(1:2/9)')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux                        
plt.savefig('/sdcard/IITH/vector/vector-4/figs/vec.pdf')
subprocess.run(shlex.split("termux-open /sdcard/IITH/vector/vector-4/figs/vec.pdf")) 
#plt.show()
