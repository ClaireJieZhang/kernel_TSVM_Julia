


import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

dminority=np.zeros((80, 4))

for i in range(0,10):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=1

for i in range(10, 20):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=1

for i in range(20,30):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=1

for i in range(30, 40):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=1

for i in range(40,50):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=-1

for i in range(50, 60):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=-1

for i in range(60,70):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=-1

for i in range(70, 80):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=-1

    
    
dnonminority=np.zeros((80, 4))

for i in range(0,10):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=1

for i in range(10, 20):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=1

for i in range(20,30):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=1

for i in range(30,40):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=1

for i in range(40,50):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=-1

for i in range(50, 60):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=-1

for i in range(60,70):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=-1

for i in range(70,80):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=-1

labeled_data=np.concatenate((dminority, dnonminority))

dminority_nolabel=np.zeros((600, 4))

for i in range(0,150):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()*-2
    dminority_nolabel[i][2]=rd.random()*4+4
    

for i in range(150, 225):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()
    dminority_nolabel[i][2]=rd.random()*4+8
    

for i in range(225, 300):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()*-1
    dminority_nolabel[i][2]=rd.random()*4+8
    
    
for i in range(300, 375):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()
    dminority_nolabel[i][2]=rd.random()*-4-8
    

for i in range(375, 450):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()*-1
    dminority_nolabel[i][2]=rd.random()*-4-8
    

for i in range(450,600):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()*2
    dminority_nolabel[i][2]=rd.random()*-4-4
    
    


    
dnonminority_nolabel=np.zeros((600, 4))

for i in range(0,150):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()*-2
    dnonminority_nolabel[i][2]=rd.random()*4+4
    


for i in range(150, 225):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()
    dnonminority_nolabel[i][2]=rd.random()*4+8

for i in range(225, 300):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()*-1
    dnonminority_nolabel[i][2]=rd.random()*4+8
    
for i in range(300, 375):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()
    dnonminority_nolabel[i][2]=rd.random()*-4-8

for i in range(375, 450):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()*-1
    dnonminority_nolabel[i][2]=rd.random()*-4-8

for i in range(450,600):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()*2
    dnonminority_nolabel[i][2]=rd.random()*-4-4

nonlabeled_data=np.concatenate((dminority_nolabel, dnonminority_nolabel))   

all_data=np.concatenate((labeled_data, nonlabeled_data))

np.set_printoptions(threshold=np.nan)

minTrans=np.transpose(dminority)
nonminTrans=np.transpose(dnonminority)


#from mpl_toolkits.mplot3d import Axes3D
#fig=plt.figure()
#ax=fig.add_subplot(111, projection='3d')

    
#minority is red o
x=minTrans[1]
y=minTrans[2]
z=minTrans[0]
#plt.plot(x, y, 'ro')
#ax.scatter(x, y, z, c='r')

#nonminority is green ^
x=nonminTrans[1]
y=nonminTrans[2]
z=nonminTrans[0]
#ax.scatter(x, y, z, c='b')

#def decision_boundary(x, y, z):
#    return 0.003x-0.25y-0.004z=

#plt.plot(x, y, 'b^')
#plt.axis([-10, 10, -20, 20])


np.savetxt("all_data.data", all_data, fmt='%0.10f', delimiter=",")

#np.savetxt("minority_800point.csv",dminority,fmt='%0.10f', delimiter=",")

#np.savetxt("nonminority_800point.csv",dnonminority,fmt='%0.10f', delimiter=",")
