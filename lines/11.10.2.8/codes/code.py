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

m = np.array([1,np.tan(np.deg2rad(30))])
i = np.array([np.cos(np.deg2rad(30))])
s = np.array(([0,1],[-1,0]))                             
n = s@m   
d = 5 
P = d / i
print(P)
#Input parameters  
A =  np.array(([10/np.sqrt(3),0]))
I =  np.array(([5*np.cos(np.deg2rad(30)),5*np.sin(np.deg2rad(30))]))
O =  np.array(([0,0])) 
n=m@s
#Generating the line   
k1=8
k2=0
x_AB = line_dir_pt(n,A,k1,k2)
x_OI = line_gen(O,I)
#Plotting all lines  
plt.plot(x_AB[0,:],x_AB[1,:],label='line')   
plt.plot(x_OI[0,:],x_OI[1,:],label='d=5')    


plt.xlabel('$ X $')
plt.ylabel('$ Y $')
plt.legend()
plt.grid(True) # minor
plt.axis('equal')
#if using termux                        
plt.savefig('/sdcard/IITH/lines/11.10.2.8/figs/fig.pdf')                                           
subprocess.run(shlex.split("termux-open /sdcard/IITH/lines/11.10.2.8/figs/fig.pdf")) 
#plt.show()
