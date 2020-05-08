import numpy as np
import collections
A = np.array([3,5,-2])
B = np.array([-3,-4,-1])
u1= np.array([2,-1,-3])
u2= np.array([2,3,-2])

Vec1 = np.array([-1,3,-3])
Vec2 = np.array([-3,2,-3])

def mag(x): 
    return np.sqrt(sum(i**2 for i in x))

def skewLinesDistance(DireA, InitA, DireB, InitB):
    d = np.dot((DireA-DireB),(np.cross(InitA,InitB)))/mag(np.cross(InitA,InitB))
    print("Skew Line Distance between ",DireA, " ", DireB, ": ", d)
    return d

def projectionOnLine(VecA, VecB):
    VecAns = VecB * np.dot(VecA, VecB) / np.dot(VecB, VecB)
    print("Projecting VecA onto Vec B: ", VecAns)
    return VecAns
def orthogonalOnLine(VecA, VecB):
    VecTemp = np.cross(VecB,np.cross(VecA, VecB))
    VecAns = VecTemp * np.dot(VecA, VecTemp) / np.dot(VecTemp, VecTemp)
    print("Projecting orthogonal VecA onto Vec B: ", VecAns)
    return VecAns
def AreaParallelogramVertices(VecA, VecB, VecC, VecD):
    VecTempList = [VecA - VecB, VecA - VecC, VecA - VecD, VecB - VecC, VecB - VecD, VecC - VecD]
    VecStringList = []
    dictOfVects = dict()
    for Vectors in VecTempList:
        elem = ','.join(map(str, Vectors))
        VecStringList.append(elem)
    VecSides = np.array([item for item, count in collections.Counter(VecStringList).items() if count > 1])
    VecPerp = np.cross(np.fromstring(VecSides[0],dtype=float, sep=','),np.fromstring(VecSides[1],dtype=float, sep=','))
    Area = np.sqrt(np.dot(VecPerp,VecPerp))
    print(Area)
    return Area

#skewLinesDistance()
projectionOnLine(np.array([3,3,-3]),np.array([5,-5,2]))
orthogonalOnLine(np.array([3,3,-3]),np.array([5,-5,2]))
AreaParallelogramVertices(np.array([-1,4,3]),np.array([0,6,7]),np.array([1,3,0]),np.array([2,5,4]))