import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
from matplotlib import cm


x_true = np.linspace(-10, 10, 100).reshape(-1,1)
y_true = 5 * x_true + 10

def fun(m, b):
    return ((y_true.reshape(1,-1) - m*x_true.T - b)**2).sum(axis=1)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
m = np.linspace(-100, 100, 50)
b = np.linspace(-1000, 1000, 50)
M, B = np.meshgrid(m, b)
Ls = fun(M.reshape(-1,1), B.reshape(-1,1))
L = Ls.reshape(M.shape)

ax.contour3D(M, B, L)

ax.set_xlabel('m axis')
ax.set_ylabel('b axis')
ax.set_zlabel('L axis')

plt.show()