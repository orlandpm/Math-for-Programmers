import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x + 1

#x = np.linspace(0,1,100)
#y = f(x)
x,y = np.meshgrid(np.linspace(0,1,100),np.linspace(0,1,100))

def g(x,y):
    return np.sqrt(np.power(x,2) + np.power(y,2))
z = g(x,y)


fig,ax = plt.subplots(figsize=(5,5))
#ax.plot(x,y)

cs = plt.contourf(x,y,z,cmap='inferno')
plt.show()
