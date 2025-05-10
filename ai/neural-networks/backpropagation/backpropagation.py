import numpy as np

X = np.array(
    [
        [0, 0, 1, 1],
        [0, 1, 0, 1]
    ]
)
Y_hat = np.array([0, 1, 1, 0])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

class NeuralNetwork:
    def __init__(self): # Output x Input ( 2 x 4 x 1)
        self.w1 = np.random.uniform(size=(4, 2)) # Four neuron, two inputs
        self.b1 = np.random.uniform(size=(4, 1)) # Four neuron, one bias
        self.w2 = np.random.uniform(size=(1, 4)) # One neuron, four inputs
        self.b2 = np.random.uniform(size=(1, 1)) # One neuron, one bias

    def foward(self, x):
        self.s1 = np.dot(self.w1, x) + self.b1
        self.z1 = sigmoid(self.s1)
        self.s2 = np.dot(self.w2, self.z1) + self.b2
        self.z2 = sigmoid(self.s2)
        return self.z2

    def backprop(self, x, y_hat, step):
        delta2 = (self.z2 - y_hat) * sigmoid_derivative(self.s2)
        delta1 = np.dot(self.w2.T, delta2) * sigmoid_derivative(self.s1)

        self.w2 -= step * np.dot(delta2, self.z1.T)
        self.b2 -= step * delta2
        self.w1 -= step * np.dot(delta1, x.T)
        self.b1 -= step * delta1

    def train(self, x, y, step, epochs):
        for i in range(epochs):
            self.foward(x)
            self.backprop(x, y, step)   

r = NeuralNetwork()

for i in range(4):
    x1, x2 = X[0, i], X[1, i]
    y = r.foward(np.array([
        [x1],
        [x2]
    ]))
    print(f"x1: {x1}, x2: {x2}, y: {y}")

for epoch in range(10000):
    err = 0.0
    for i in range(4):
        x1, x2 = X[0, i], X[1, i]
        y_hat = Y_hat[i]
        y = r.foward(np.array([
            [x1],
            [x2]
        ]))
        err += (y - y_hat) ** 2
        r.backprop(np.array([
            [x1],
            [x2]
        ]), y_hat, 0.5)
    print(f"Epoch {epoch}, Error: {err}")


