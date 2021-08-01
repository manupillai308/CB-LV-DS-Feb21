import numpy as np

class Dot:
    def __init__(self, input_size, units):
        self.W = np.random.randn(input_size, units)
        self.b = np.random.randn(units, 1)

    def __call__(self, X):
        return self.W.T.dot(X) + self.b

    def grad_w(self, X):
        I = np.identity(self.b.shape[0])
        grad = np.stack([I]*self.W.shape[0], axis=1)*X
        return np.transpose(grad, [1, 0, 2])
    
    def grad_b(self):
        return np.identity(self.b.shape[0])

    def grad_input(self):
        return self.W.T
    
    def get_output_size(self):
        return self.b.shape
    
    def get_no_of_params(self):
        return np.prod(self.W.shape) + np.prod(self.b.shape)
    
    def update(self, gradW, gradb, optimizer, method):
        if method == "minimize":
            self.W = optimizer.minimize(self.W, gradW)
            self.b = optimizer.minimize(self.b, gradb)
        elif method == "maximize":
            self.W = optimizer.maximize(self.W, gradW)
            self.b = optimizer.maximize(self.b, gradb)


class Dense:
    
    def __init__(self, units, activation, input_size):
        self.units = units
        self.dot = Dot(input_size, units)
        self.activation = activation
        self.input_size = input_size

    def get_output_size(self):
        return self.dot.get_output_size()

    def get_no_of_params(self):
        return self.dot.get_no_of_params()

    def eval(self, X):
        return self.activation(self.dot(X))

    def grad_parameters(self, X):
        da_dI = self.activation.grad_input(self.dot(X))
        dI_dw = self.dot.grad_w(X)
        da_dw = da_dI.dot(dI_dw)
        dI_db = self.dot.grad_b()
        da_db = da_dI.dot(dI_db)
        return (np.transpose(da_dw, [1,0,2]), da_db)
    
    def grad_input(self, X):
        g1 = self.activation.grad_input(self.dot(X))

        g2 = self.dot.grad_input()

        return g1.dot(g2)
    
    def update(self, grad_w, grad_b, optimizer, method="minimize"):
        self.dot.update(grad_w, grad_b, optimizer, method)
        