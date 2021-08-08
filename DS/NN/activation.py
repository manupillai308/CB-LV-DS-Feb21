# from DS.NN.test import X
import numpy as np
from numpy.core.fromnumeric import shape

class Sigmoid:
    def __call__(self, X):
        return self.eval(X)
    
    def eval(self, X):
        return 1/(1+np.e**(-1*X))

    def grad_input(self, X):
        re = np.einsum('ij,im->mij', np.identity(X.shape[0]), self.eval(X)*(1 - self.eval(X)))
        return re
class Relu:
    def __call__(self,X):
        return self.eval(X)

    def eval(self, X):
        X = X.copy()
        for l in X:
            for i in range(0,len(l)):
                l[i] = np.max([0, l[i]])
        return X

    def grad_input(self,X):
        X = X.copy()
        for l in X:
            for i in range(0,len(l)):
                if l[i]<=0:
                    l[i] = 0
                else:
                    l[i] = 1
        
        re = np.einsum('ij,im->mij', np.identity(X.shape[0]), X)
        return re
        