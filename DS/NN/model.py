import numpy as np

class Sequential:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.outputs = []

    def add(self, layer):
        self.layers.append(layer)
        return self
    
    def summary(self):
        from tabulate import tabulate

        headers = ["Layer Type", "Output Shape", "No. of parameters"]
        summary_ = []
        params = 0
        for layer in self.layers:
            p = layer.get_no_of_params()
            params += p
            summary_.append([layer.__class__.__name__, layer.get_output_size(), p])
        
        print(tabulate(summary_, headers=headers))
        print("Total No. of parameters:", params)
    
    def fit(self, X, y, n_epochs, learning_rate, optimizer, batch_size=1, verbose=1):
        self.optimizer = optimizer.set_lr(learning_rate)
        for i in range(n_epochs):
            if verbose == 1:
                print(f"Epoch: {i+1}") 
            gradients = []
            for j in range(X.shape[0]):
                _, outputs, _gradients_ = self.forward_propagation(X[j].reshape(1,-1))
                grads = self.backward_propagation(outputs, _gradients_, y[j].reshape(1,-1))
                gradients.append(grads)
                if (j+1) % batch_size == 0:
                    self._update_params(gradients)
                    gradients = []
                    losses = []
                    if verbose == 1:
                        print(f"\rLoss:{self._eval_loss(X, y)}", end="")
            if verbose == 1:
                print("")
            if verbose == 0:
                print(f"\rEpoch: {i+1} Loss:{self._eval_loss(X, y)}", end="")
            
        print("")
            
    def forward_propagation(self, X, eval=False):
        output = X.T
        outputs = [output]
        gradients = []
        for layer in self.layers:
            if not eval:
                grad_ = {}
                grad_["input"] = layer.grad_input(output)
                grad_["w"], grad_["b"] = layer.grad_parameters(output)
                gradients.append(grad_)
            output = layer.eval(output)
            outputs.append(output)

        return output.T, outputs, gradients
    
    def backward_propagation(self, outputs, gradients, y):
        grad_loss = self.loss.grad_input(outputs[-1], y)
        outputs = outputs[:-1]
        grads = []
        for grad, output in list(zip(gradients, outputs))[::-1]:
            grad_w, grad_b = grad_loss.dot(grad["w"])[0], grad_loss.dot(grad["b"]).T
            grads.append((grad_w, grad_b))
            grad_loss = grad_loss.dot(grad["input"])
        
        return grads
    
    def _update_params(self, gradients):
        grads = [[0, 0] for _ in gradients[0]]
        for grads_ in gradients:
            for i in range(len(grads_)):
                grads[i][0] += grads_[i][0]
                grads[i][1] += grads_[i][1]

        for ((grad_w, grad_b), layer) in zip(grads, self.layers[::-1]):
            layer.update(grad_w, grad_b, self.optimizer)

    def _eval(self, X):
        return self.forward_propagation(X, eval=True)[0]
    
    def compile(self, loss):
        self.loss = loss

    def _eval_loss(self, X, y_true):
        if self.loss is None:
            raise RuntimeError("Model not compiled")
            
        return self.loss(self._eval(X), y_true)