#Drawing a rectangle

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#Rectangle vertices
A = np.array([-3,1]) 
B = np.array([0.0153842,2.723]) 
C = np.array([1,1]) 
D = np.array([-2.01,-0.72]) 

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux                        
plt.savefig('/sdcard/IITH/matrix/line/line.pdf')                                
plt.savefig('/sdcard/IITH/matrix/line/line.eps')                                
subprocess.run(shlex.split("termux-open /sdcard/IITH/matrix/line/line.pdf")) 
#else       
#plt.show()
