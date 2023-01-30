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


#Point A and B
A = np.array([10/np.sqrt(3),0]) 
B = np.array([0,10]) 
O = np.array([0,0])
M = np.array([5*np.sqrt(3)/2,5/2])
#Generating all lines
x_AB = line_gen(A,B)
x_OM =line_gen(O,M)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$Line$')
plt.plot(A[0], A[1])
#plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1])
#plt.text(B[0] * (1 - 0.1), B[1] * (1) , 'B')
plt.plot(x_OM[0,:],x_OM[1,:],label='$Perpendicular-from-Origin$')
plt.plot(O[0], O[1])
plt.text(O[0] * (1 + 0.5), O[1] * (1 - 0.5) , 'O')
plt.plot(M[0], M[1], 'o')
#plt.text(M[0] * (1 - 0.2), M[1] * (1) , 'M')


plt.xlabel('$ X $')
plt.ylabel('$ Y $')
plt.legend()
plt.grid(True) # minor
plt.axis('equal')
#if using termux                        
plt.savefig('/sdcard/IITH/lines/11.10.2.8/figs/fig.pdf')                                           
subprocess.run(shlex.split("termux-open /sdcard/IITH/lines/11.10.2.8/figs/fig.pdf")) 
#plt.show()
