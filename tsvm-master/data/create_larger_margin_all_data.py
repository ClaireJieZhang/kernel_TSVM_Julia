


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
    dminority[i][3]=1

for i in range(200,300):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=1

for i in range(300, 400):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*2+1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=1

for i in range(400,500):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=-1

for i in range(500, 600):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*4
    dminority[i][3]=-1

for i in range(600,700):
    dminority[i][0]=-1
    dminority[i][1]=rd.random()*-2-1
    dminority[i][2]=rd.random()*-4
    dminority[i][3]=-1

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
    dnonminority[i][3]=1

for i in range(200,300):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=1

for i in range(300,400):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*2+1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=1

for i in range(400,500):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=-1

for i in range(500, 600):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*4
    dnonminority[i][3]=-1

for i in range(600,700):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=-1

for i in range(700,800):
    dnonminority[i][0]=1
    dnonminority[i][1]=rd.random()*-2-1
    dnonminority[i][2]=rd.random()*-4
    dnonminority[i][3]=-1

labeled_data=np.concatenate((dminority, dnonminority))

dminority_nolabel=np.zeros((6000, 4))

for i in range(0,1500):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()*-2
    dminority_nolabel[i][2]=rd.random()*4+4
    

for i in range(1500, 2250):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()
    dminority_nolabel[i][2]=rd.random()*4+8
    

for i in range(2250, 3000):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()*-1
    dminority_nolabel[i][2]=rd.random()*4+8
    
    
for i in range(3000, 3750):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()
    dminority_nolabel[i][2]=rd.random()*-4-8
    

for i in range(3750, 4500):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()*-1
    dminority_nolabel[i][2]=rd.random()*-4-8
    

for i in range(4500,6000):
    dminority_nolabel[i][0]=-1
    dminority_nolabel[i][1]=rd.random()*2
    dminority_nolabel[i][2]=rd.random()*-4-4
    
    


    
dnonminority_nolabel=np.zeros((6000, 4))

for i in range(0,1500):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()*-2
    dnonminority_nolabel[i][2]=rd.random()*4+4
    


for i in range(1500, 2250):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()
    dnonminority_nolabel[i][2]=rd.random()*4+8

for i in range(2250, 3000):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()*-1
    dnonminority_nolabel[i][2]=rd.random()*4+8
    
for i in range(3000, 3750):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()
    dnonminority_nolabel[i][2]=rd.random()*-4-8

for i in range(3750, 4500):
    dnonminority_nolabel[i][0]=1
    dnonminority_nolabel[i][1]=rd.random()*-1
    dnonminority_nolabel[i][2]=rd.random()*-4-8

for i in range(4500,6000):
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
x=labeled_data[:,1]
y=labeled_data[:,2]
z=labeled_data[:,3]

for i in range(len(z)):
    if z[i]==1:
        plt.plot(x[i], y[i], 'ro')
       
    if z[i]==-1:
        plt.plot(x[i], y[i], 'b^')
  
#ax.scatter(x, y, z, c='r')

    
plt.axis([-10, 10, -20, 20])


np.savetxt("linear_two_classes.data", labeled_data[:,1:4], fmt='%0.10f', delimiter=",")

#np.savetxt("minority_800point.csv",dminority,fmt='%0.10f', delimiter=",")

#np.savetxt("nonminority_800point.csv",dnonminority,fmt='%0.10f', delimiter=",")
