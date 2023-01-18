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

#Rank of the Matrix
my_matrix = np.array([[2 ,-3 ,4], [-4, 6, -8    ]])
print("Matrix")
for row in my_matrix:
  print(row)
rank = np.linalg.matrix_rank(my_matrix)
print("Rank of the Matrix is : ",rank)

#1 Point
I = np.array([-1.5,0]) 
J = np.array([1,0])   
K = np.array([2,0])
#1 Generating all lines
x_IJ = line_gen(I,J)
x_JK = line_gen(J,K)
x_KI = line_gen(K,I)

#1 Plotting all lines
plt.plot(x_IJ[0,:],x_IJ[1,:],label='$A$')
plt.plot(x_JK[0,:],x_JK[1,:],label='$B$')

#1 plotting the all point
plt.plot(I[0], I[1], 'o',color='b')
plt.plot(J[0], J[1], 'o',color='b')
plt.plot(K[0], K[1], 'o',color='b')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux                        
plt.savefig('/sdcard/IITH/vectors/12.10.2.11/figs/fig.pdf')                                           
subprocess.run(shlex.split("termux-open /sdcard/IITH/vectors/12.10.2.11/figs/fig.pdf")) 
#plt.show()
