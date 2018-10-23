

'''
import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


all_data=np.loadtxt("combined_data.data", delimiter=",")




fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

for one_point in all_data:
    #if one_point[3]==0:
 #       ax.scatter(one_point[0], one_point[1], one_point[2], c='r', marker='o')
    if one_point[3]==-1:
        ax.scatter(one_point[0], one_point[1], one_point[2], c='b', marker='^')
    if one_point[3]==1:
        ax.scatter(one_point[0], one_point[1], one_point[2], c='g', marker='+')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-3,3)
ax.set_zlim3d(-4,6)

plt.show()
'''


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set


# create x,y
xx, yy = np.meshgrid(range(-2, 2), range(-4, 4))

# calculate corresponding z
#z = (-4.673 * xx - normal[1] * yy - d) * 1. /normal[2]
z1 = (-4.673*xx + 11.625 * yy +0.6)*1/-2.58

z2 = (-0.7946*xx + 1.87896*yy +0.1) * 1/-0.3742

# plot the surface
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z1, color='y', alpha=0.2,label='yellow-SVM, blue-TSVM')
plt3d.plot_surface(xx, yy, z2, alpha=0.2)

ax = plt.gca()
ax.hold(True)



all_data=np.loadtxt("combined_data.data", delimiter=",")


for one_point in all_data:
    if one_point[3]==0:
        ax.scatter(one_point[0], one_point[1], one_point[2], c='r', marker='o')
    #if one_point[3]==-1:
#        ax.scatter(one_point[0], one_point[1], one_point[2], c='b', marker='^')
#    if one_point[3]==1:
#        ax.scatter(one_point[0], one_point[1], one_point[2], c='g', marker='+')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z1 and Z2 Label')

ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-3,3)
ax.set_zlim3d(-4,6)

plt.show()


