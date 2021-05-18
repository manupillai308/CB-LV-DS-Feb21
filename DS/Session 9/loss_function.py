import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
from matplotlib import cm


def squared_loss(X, y, m, b):
    return ((y.reshape(1,-1) - m*X.T - b)**2).sum(axis=1)

def plot_loss(X, y, losses, parameters, fun=squared_loss):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m = np.linspace(0, 10, 50)
    b = np.linspace(0, 10, 50)
    M, B = np.meshgrid(m, b)
    Ls = fun(X, y, M.reshape(-1,1), B.reshape(-1,1))
    L = Ls.reshape(M.shape)

    # ax.contour3D(M, B, L)
    
    surf = ax.plot_surface(M, B, L,cmap=cm.coolwarm, alpha=0.5)
    # surf = ax.scatter(M, B, L,cmap=cm.coolwarm, alpha=0.5)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.scatter(parameters[:, 1], parameters[:, 0], losses, color="red")

    ax.set_xlabel('m axis')
    ax.set_ylabel('b axis')
    ax.set_zlabel('L axis')

    plt.show()