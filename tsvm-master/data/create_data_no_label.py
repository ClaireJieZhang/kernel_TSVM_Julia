


import numpy as np
import pandas as pd
import random as rd

d=np.zeros((3000, 2))

#for i in range(0,75):
#    d[i][0]=1
#    d[i][1]=rd.random()*2
   # d[i][2]=rd.randint(3,8)
#    d[i][2]=1
   

#for i in range(75, 100):
#    d[i][0]=1
#    d[i][1]=rd.random()*-0.25
 #   d[i][2]=rd.randint(-12,-8)
#    d[i][2]=1

#for i in range(100, 125):
#    d[i][0]=1
#    d[i][1]=rd.random()*-0.5
 #   d[i][2]=rd.randint(-12,-8)
#    d[i][2]=-1
  
    
#for i in range(125, 150):
#    d[i][0]=-1
#    d[i][1]=rd.random()*4
 #   d[i][2]=rd.randint(3,8)
#    d[i][2]=1

#for i in range(150, 175):
#    d[i][0]=-1
#    d[i][1]=rd.random()*1
 #   d[i][2]=rd.randint(3,8)
#    d[i][2]=-1
    
#for i in range(175, 200):
#    d[i][0]=-1
#    d[i][1]=rd.random()*0.5
 #   d[i][2]=rd.randint(-8,-3)
#    d[i][2]=-1

#for i in range(200, 250):
#    d[i][0]=-1
#    d[i][1]=rd.random()*-2
 #   d[i][2]=rd.randint(-8,-3)
#    d[i][2]=-1






for i in range(1,750):
    d[i][0]=1
    d[i][1]=rd.random()*2
   # d[i][2]=rd.randint(3,8)
 #   d[i][2]=1
   

for i in range(750, 1500):
    d[i][0]=1
    d[i][1]=rd.random()*-2
 #   d[i][2]=rd.randint(-12,-8)
 #   d[i][2]=1

for i in range(1500, 2250):
    d[i][0]=-1
    d[i][1]=rd.random()*2
 #   d[i][2]=rd.randint(-12,-8)
 #   d[i][2]=-1
  
    
for i in range(2250, 3000):
    d[i][0]=-1
    d[i][1]=rd.random()*-2
 #   d[i][2]=rd.randint(3,8)
 #   d[i][2]=1



np.set_printoptions(threshold=np.nan)

print d

np.savetxt("sdata_no_label_all.csv",d,fmt='%0.10f', delimiter=",")


