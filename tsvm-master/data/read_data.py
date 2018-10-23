import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = np.loadtxt('all_data.data', delimiter=",")

dataTranspose=np.transpose(data)

print data
print "##########################"
print dataTranspose

x=dataTranspose[1]
y=dataTranspose[2]
z=dataTranspose[3]

fig=plt.figure()
fig.suptitle('color indicate label (+, - or placeholder - not labelled)', fontsize=12, fontweight='bold')
ax = fig.add_subplot(111)

ax.scatter(x, y, c = z)

t=np.arange(-3, 3, 0.01)

def svm_boundary(t):
    return 80.5523*t+1.55157

def tsvm_boundary(t):
    return 5.4785*t + 0.4733

ax.plot(t, tsvm_boundary(t), 'k')

plt.show()
