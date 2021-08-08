from model import Sequential
from layer import Dense
from loss import BinaryCrossEntropy
from activation import Sigmoid, Relu
from optimizer import GradientDescentOptimizer

model = Sequential()
model.add(Dense(units=3, activation=Relu(), input_size=2))
model.add(Dense(units=2, activation=Relu(), input_size=3))
model.add(Dense(units=1, activation=Sigmoid(), input_size=2))
model.compile(BinaryCrossEntropy())

model.summary()

from sklearn.datasets import make_gaussian_quantiles
X, y = make_gaussian_quantiles(n_samples=200,n_classes=2)
y = y.reshape(-1,1)


model.fit(X, y, n_epochs=2000, batch_size=200, learning_rate=0.002, optimizer=GradientDescentOptimizer(), verbose=1)