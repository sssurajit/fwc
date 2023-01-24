import numpy as np

A = np.array([0, -1/np.sqrt(2),1/np.sqrt(2)])
r = (A.T@A)
print("unit :",r)

B1 = np.array([1,0,0])
a1 = (A.T@B1)
print("Cos 1 :",a1)

B2 = np.array([0,1,0])
a2 = (A.T@B2)
print("Cos 2 :",a2)

B3 = np.array([0,0,1])
a3 = (A.T@B3)
print("Cos 3 :",a3)

