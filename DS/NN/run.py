from model import Sequential
from layer import Dense
from loss import BinaryCrossEntropy
from activation import Sigmoid
from optimizer import GradientDescentOptimizer

if __name__ == "__main__":
    model = Sequential()
    model.add(Dense(units=3, activation=Sigmoid(), input_size=2))
    model.add(Dense(units=2, activation=Sigmoid(), input_size=3))
    model.add(Dense(units=1, activation=Sigmoid(), input_size=2))
    model.compile(BinaryCrossEntropy())
    model.summary()

    from sklearn.datasets import make_gaussian_quantiles
    X, y = make_gaussian_quantiles(n_samples=200,n_classes=2)
    y = y.reshape(-1,1)
    print("Loss", model.evaluate(X, y)[0])
    model.fit(X, y, n_epochs=1000, batch_size=1, learning_rate=0.003, optimizer=GradientDescentOptimizer(), verbose=1)