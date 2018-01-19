import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

i = complex(0, 1)
height = range(0,1,)
real = []
imag = []

def Turm(x, n):
    result = 0
    for _ in range(0, n + 1):
        result = x**result
    return result


for a in range(1, 40):
    r = Turm(i, a)
    dist = math.sqrt((r.real)**2 + (r.imag)**2)
    # height.append(a)
    real.append(r.real)
    imag.append(r.imag)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = real, imag, height
ax.plot3D(x, y, z)
plt.show()
