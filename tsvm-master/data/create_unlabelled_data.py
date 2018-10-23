


import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

dminority=np.zeros((6000, 3))

for i in range(0,1500):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2
    dminority[i][2]=rd.random()*4+4


for i in range(1500, 2250):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()
    dminority[i][2]=rd.random()*4+8

for i in range(2250, 3000):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-1
    dminority[i][2]=rd.random()*4+8
    
for i in range(3000, 3750):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()
    dminority[i][2]=rd.random()*-4-8

for i in range(3750, 4500):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-1
    dminority[i][2]=rd.random()*-4-8

for i in range(4500,6000):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2
    dminority[i][2]=rd.random()*-4-4
    


    
dnonminority=np.zeros((6000, 3))

for i in range(0,1500):
    dnonminority[i][0]=-1
    dnonminority[i][1]=rd.random()*-2
    dnonminority[i][2]=rd.random()*4+4


for i in range(1500, 2250):
    dnonminority[i][0]=-1
    dnonminority[i][1]=rd.random()
    dnonminority[i][2]=rd.random()*4+8

for i in range(2250, 3000):
    dnonminority[i][0]=-1
    dnonminority[i][1]=rd.random()*-1
    dnonminority[i][2]=rd.random()*4+8
    
for i in range(3000, 3750):
    dnonminority[i][0]=-1
    dnonminority[i][1]=rd.random()
    dnonminority[i][2]=rd.random()*-4-8

for i in range(3750, 4500):
    dnonminority[i][0]=-1
    dnonminority[i][1]=rd.random()*-1
    dnonminority[i][2]=rd.random()*-4-8

for i in range(4500,6000):
    dnonminority[i][0]=-1
    dnonminority[i][1]=rd.random()*2
    dnonminority[i][2]=rd.random()*-4-4

    
np.set_printoptions(threshold=np.nan)

minTrans=np.transpose(dminority)
nonminTrans=np.transpose(dnonminority)

#minority is red o
x=minTrans[1]
y=minTrans[2]
plt.plot(x, y, 'ro')

#nonminority is green ^
x=nonminTrans[1]
y=nonminTrans[2]
plt.plot(x, y, 'b^')
plt.axis([-15, 15, -30, 30])
unlabeled_data=np.concatenate((dminority, dnonminority))

np.savetxt("unlabelled_12000points.data", labeled_data, fmt='%0.10f', delimiter=",")

np.savetxt("minority_800point.csv",dminority,fmt='%0.10f', delimiter=",")

np.savetxt("nonminority_800point.csv",dnonminority,fmt='%0.10f', delimiter=",")
