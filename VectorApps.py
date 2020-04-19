import numpy as np
A = np.array([3,5,-2])
B = np.array([-3,-4,-1])
u1= np.array([2,-1,-3])
u2= np.array([2,3,-2])

def mag(x): 
    return np.sqrt(sum(i**2 for i in x))

def skewLinesDistance():
    d = np.dot((A-B),(np.cross(u1,u2)))/mag(np.cross(u1,u2))
    return d

print(skewLinesDistance())