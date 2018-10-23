


import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

dminority=np.zeros((800, 4))

for i in range(0,100):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=1

for i in range(100, 200):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=-1

for i in range(200,300):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=1

for i in range(300, 400):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=-1

for i in range(400,500):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=1

for i in range(500, 600):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=-1

for i in range(600,700):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=1

for i in range(700, 800):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=-1

    
    
dnonminority=np.zeros((800, 4))

for i in range(0,100):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=1

for i in range(100, 200):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=-1

for i in range(200,300):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=1

for i in range(300,400):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=-1

for i in range(400,500):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=1

for i in range(500, 600):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=-1

for i in range(600,700):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=1

for i in range(700,800):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=-1

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
plt.axis([-10, 10, -20, 20])
labeled_data=np.concatenate((dminority, dnonminority))

np.savetxt("labelled_1600points.data", labeled_data, fmt='%0.10f', delimiter=",")

np.savetxt("minority_800point.csv",dminority,fmt='%0.10f', delimiter=",")

np.savetxt("nonminority_800point.csv",dnonminority,fmt='%0.10f', delimiter=",")
