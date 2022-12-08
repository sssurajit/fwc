import numpy as np
omat = np.array([[0,1],[-1,0]]) 

#Line L1 calculation
A = np.array([3,7]).reshape(2,1)
B = np.array([6,5]).reshape(2,1)
m = A-B
n = omat@m
print(n)
print(n.T@A)

#intersection point calculation of L1 and L2
K = np.array([5,6,2,3]).reshape(2,2)
b = np.array([56,27]).reshape(2,1)
print(np.linalg.inv(K)@b)
