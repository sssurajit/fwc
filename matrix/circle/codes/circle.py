import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
import sympy as sp
import sys  #for path to external scripts
import subprocess
import shlex

#local imports
#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen 

#Generating points on a circle
def circ_gen(O,r):
  len = 100
  theta = np.linspace(0,2*np.pi,len)
  x_circ = np.zeros((2,len))
  x_circ[0,:] = r*np.cos(theta)
  x_circ[1,:] = r*np.sin(theta)
  x_circ = (x_circ.T + O).T
  return x_circ


#Input parameters
A = np.array(([3,7]))    #point(a) on circle1
B = np.array(([6,5]))    #point(b) on circle1
#Centre and radius of circle1
u1 = np.array(([4.5,6]))
u2 = np.array(([2,3]))
u3 = np.array(([3.5,4.5]))
u4 = np.array(([2.5,3]))



plt.axline(A,B, color='gray', linestyle='--',label='$Locus$')

#Computation of  radius of circle(1,2,3,4)
r1 = LA.norm(u1-A)
r2 = 4
r3 = np.sqrt(6.5)
#r4 = np.sqrt(16.25)

#Generating the circle
x_circ1= circ_gen(u1,r1) 
x_circ2= circ_gen(u2,r2)
x_circ3= circ_gen(u3,r3)
#x_circ4= circ_gen(u4,r4)

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')


#Plotting the circle

plt.plot(x_circ1[0,:],x_circ1[1,:],color='green',label='$Circle1$')
plt.plot(x_circ2[0,:],x_circ2[1,:],color='red',label='$Circle2$')
plt.plot(x_circ3[0,:],x_circ3[1,:],color='blue',label='$Circle3$')
#plt.plot(x_circ4[0,:],x_circ3[1,:],color='orange',label='$Circle4$')

#Labeling the coordinates
tri_coords = np.vstack((A,B,u1,u2,u3)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A(3,7)','B(6,5)','u1','u2','u3']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
            (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
            textcoords="offset points", # how to position the text
            xytext=(0,10), # distance from text to points (x,y)
            ha='center') # horizontal alignment can be left, right or center



plt.xlabel('$ X $')
plt.ylabel('$ Y $')
plt.legend()
plt.grid(True) # minor
plt.axis('equal')
#plt.title('Locus of center of circle')
plt.savefig('/sdcard/IITH/matrix/circle/circle/fig.jpg')
plt.savefig('/sdcard/IITH/matrix/circle/circle.pdf')
subprocess.run(shlex.split("termux-open /sdcard/IITH/matrix/circle/circle.pdf"))
#plt.show()



