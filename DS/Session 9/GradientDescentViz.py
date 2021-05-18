

import numpy as np
import matplotlib.pyplot as plt

# X, y = np.load("../Data/LinearRegression/X_data.npy"), np.load("../Data/LinearRegression/Y_data.npy").reshape(-1,1)


# X.shape, y.shape



class LinearRegression:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate
    
    def predict(self, X):
        return X.dot(self.W)

    def get_gradient(self, X, y):
        gradient = []

        for i in range(X.shape[1]): # n+1
            gradient.append((2 * (y - self.predict(X)) * -X[:, i].reshape(-1,1)).sum()) # safe approach is always provide axis
        
        return np.array(gradient).reshape(-1,1)

    def r2_score(self, X, y):
        return 1 - (self.loss(self.predict(X), y)/self.loss(y, y.mean()))

    def loss(self, y_true, y_pred):
        return ((y_true - y_pred)**2).sum()
    
    def sum_of_residuals(self, X, y):
        return (y - self.predict(X)).sum()
    
    def batch_gradient_descent(self, X, y, n_epochs=500):
        X = np.copy(X)
        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1) #constant column added
        self.W = np.random.randn(X.shape[1], 1)
        losses = []
        parameters = []
        for i in range(n_epochs):
            self.W = self.W - self.learning_rate*self.get_gradient(X, y)
            loss = self.loss(y, self.predict(X))
            print("\r"+f"epoch: {i+1}, loss: {loss}, acc: {self.r2_score(X, y)},SOR: {self.sum_of_residuals(X, y)}", end="")
            losses.append(loss)
            parameters.append(self.W.copy())

        return np.array(losses), np.array(parameters)

    def mini_batch_gradient_descent(self, X, y, n_epochs=500, batch_size=10):
        X = np.copy(X)
        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1) #constant column added
        self.W = np.random.randn(X.shape[1], 1)
        losses = []
        parameters = []
        for i in range(n_epochs):
            random_indexes = np.random.choice(np.arange(0, X.shape[0]), size=batch_size)
            X_batch = X[random_indexes]

            self.W = self.W - self.learning_rate*self.get_gradient(X_batch, y[random_indexes])
            loss = self.loss(y, self.predict(X))
            print("\r"+f"epoch: {i+1}, loss: {loss}, acc: {self.r2_score(X, y)}, SOR: {self.sum_of_residuals(X, y)}", end="")
            losses.append(loss)
            parameters.append(self.W.copy())
        
        return np.array(losses), np.array(parameters)

    def fit(self, X, y, method="batch", **kwargs):

        if method == "batch":
            losses, parameters = self.batch_gradient_descent(X, y, **kwargs)
        
        elif method == "mini_batch":
            losses, parameters = self.mini_batch_gradient_descent(X, y, **kwargs)
        
        elif method == "stochastic":
            losses, parameters = self.mini_batch_gradient_descent(X, y, batch_size=1)


        return losses, parameters



# lr = LinearRegression(learning_rate=0.005)
# losses = lr.fit(X, y, n_epochs=20)
# plt.plot(losses)
# plt.show()



# lr = LinearRegression(learning_rate=0.005)
# losses = lr.fit(X, y, n_epochs=20, method="mini_batch", batch_size=30)
# plt.plot(losses)
# plt.show()


from loss_function import plot_loss



X_1d = np.linspace(-10, 10, 100).reshape(-1,1)
X_1d = (X_1d - X_1d.min(axis=0))/(X_1d.max(axis=0) - X_1d.min(axis=0))
y_1d = 5 * X_1d + 10 + 0.3*np.random.randn(X_1d.shape[0], 1)

lr = LinearRegression(learning_rate=0.005)
losses, parameters = lr.fit(X_1d, y_1d, n_epochs=1000, method="mini_batch", batch_size=5)



# plt.scatter(X_1d, y_1d)
# plt.show()



plot_loss(X_1d, y_1d, losses, parameters)

