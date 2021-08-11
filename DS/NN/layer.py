import numpy as np

class Dot:
    def __init__(self, input_size, units):
        self.W = np.random.randn(input_size, units)
        self.b = np.random.randn(units, 1)

    def __call__(self, X):
        return self.W.T.dot(X) + self.b

    def grad_w(self, X):
        I = np.identity(self.b.shape[0])
        m1 = np.stack([I]*self.W.shape[0], axis=1)
        grad = np.einsum('ijk,jm->mijk', m1, X)
        return grad
    
    def grad_b(self, X):
        return np.stack([np.identity(self.b.shape[0])]*X.shape[1], axis=0)

    def grad_input(self, X):
        return np.stack([self.W.T]*X.shape[1], axis=0)
    
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
        if isinstance(input_size, tuple):
            if len(input_size) <= 2:
                input_size = input_size[0]
            else:
                raise RuntimeError(f"Incompatible input shape, got {input_size}")
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
        da_dw = np.einsum('mij,mjkl->mikl', da_dI, dI_dw)
        
        dI_db = self.dot.grad_b(X)
        da_db = np.einsum('mij,mjk->mik', da_dI, dI_db)
        return (da_dw, da_db)
    
    def gradient_dict(self, output):
        grad_ = {}
        grad_["input"] = self.grad_input(output)
        grad_["w"], grad_["b"] = self.grad_parameters(output)

        return grad_


    def grad_input(self, X):
        g1 = self.activation.grad_input(self.dot(X))

        g2 = self.dot.grad_input(X)

        return np.einsum('mij,mjk->mik', g1, g2)
    
    @staticmethod
    def backprop_grad(grad_loss, grad):
        grad_w = np.einsum('mij,mjkl->mikl', grad_loss, grad["w"]).sum(axis=0)[0]
        grad_b = np.einsum('mij,mjk->mik', grad_loss, grad["b"]).sum(axis=0).T
        grad_loss = np.einsum('mij,mjk->mik', grad_loss, grad["input"])

        return grad_w, grad_b, grad_loss

    def update(self, grad_w, grad_b, optimizer, method="minimize"):
        self.dot.update(grad_w, grad_b, optimizer, method)
        