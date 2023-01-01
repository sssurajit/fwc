import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys
lib_path = '/sdcard/IITH/matrix/CoordGeo'
sys.path.insert(0,lib_path)

#local import
from line.funcs import *
from triangle.funcs import *

#if using termux
import subprocess
import shlex
#end if

#Point A and B
A = np.array([0,0]) 
B = np.array([36,15])   
C = np.array([36,0])

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],color='orange',label='$AB=39$')
plt.plot(x_BC[0,:],x_BC[1,:],color='gray',linestyle="--")
plt.plot(x_CA[0,:],x_CA[1,:],color='gray',linestyle="--")
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux                        
plt.savefig('/sdcard/IITH/vector/vector.pdf')                                           
subprocess.run(shlex.split("termux-open /sdcard/IITH/vector/vector.pdf")) 
#plt.show()
