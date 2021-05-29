import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
from matplotlib import cm


def squared_loss(X, y, m, b):
    return ((y.reshape(1,-1) - m*X.T - b)**2).sum(axis=1)

def plot_loss(X, y, fun=squared_loss):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m = np.linspace(-2, 2, 100)
    b = np.linspace(-10, 10, 100)
    M, B = np.meshgrid(m, b)
    Ls = fun(X, y, M.reshape(-1,1), B.reshape(-1,1))
    L = Ls.reshape(M.shape)

    # ax.contour3D(M, B, L)
    surf = ax.plot_surface(M, B, L,cmap=cm.coolwarm)
    fig.colorbar(surf, shrink=0.5, aspect=5)

    ax.set_xlabel('m axis')
    ax.set_ylabel('b axis')
    ax.set_zlabel('L axis')

    plt.show()

if __name__ == "__main__":
    x_A = 1.7 * np.random.randn(50) + 13
    x_B = 3.5 * np.random.randn(50) + 60

    X_data = np.concatenate([x_A, x_B], axis=0).reshape(-1,1)
    y_data = np.concatenate([np.ones_like(x_A), np.zeros_like(x_B)], axis=0)

    def sigmoid(Z):
        return 1/(1 + (np.e)**-Z)

    def squared_loss_with_sigmoid(X, y, m, b):
        y_pred = sigmoid(m*X.T + b)
        return ((y.reshape(1,-1) - y_pred)**2).sum(axis=1)

    def log_loss(X, y, m, b):
        y_true = y
        y_pred = sigmoid(m*X.T + b)
        ix_zeros = np.arange(0, y_true.shape[0])[y_true.reshape(-1) == 0]
        ix_ones = np.arange(0, y_true.shape[0])[y_true.reshape(-1) == 1]
        
        y_zero = np.log(1 - y_pred[:, ix_zeros] + 1e-10).sum(axis=1)
        y_one = np.log(y_pred[:, ix_ones] + 1e-10).sum(axis=1)

        return -1 * (y_zero + y_one)


    plot_loss(X_data, y_data, fun=squared_loss_with_sigmoid)
    plot_loss(X_data, y_data, fun=log_loss)
