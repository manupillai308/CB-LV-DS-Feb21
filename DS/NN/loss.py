import numpy as np

class BinaryCrossEntropy:
    def __init__(self):
        pass

    def __call__(self, y_pred, y_true):
        ix_zeros = np.arange(0, y_true.shape[0])[y_true.reshape(-1) == 0]
        ix_ones = np.arange(0, y_true.shape[0])[y_true.reshape(-1) == 1]

        y_zero = np.log(1 - y_pred[ix_zeros] + 1e-10).sum()
        y_one = np.log(y_pred[ix_ones] + 1e-10).sum()

        return -1 * (y_zero + y_one)
    
    def grad_input(self, X, y_true):
        if y_true == 0:
            return 1/(1-X)
        else:
            return -1/X 
        
