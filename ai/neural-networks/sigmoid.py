import numpy as np
from matplotlib import pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class Neuron:
    def __init__(self, input_size=5):
        self.w = np.random.random(input_size)  # Pesos aleatórios
        self.b = np.random.random()  # Viés aleatório

    def compute(self, inputs):
        s = np.dot(self.w, inputs) + self.b  # Soma ponderada
        z = sigmoid(s)  # Aplicação da função sigmoide
        return z

class Neuron:
    def __init__(self, weights, bias):
        self.w = np.array(weights)
        self.b = bias

    def compute(self, inputs):
        s = np.dot(self.w, inputs) + self.b
        z = np.tanh(s)
        return z
    
neuron = Neuron(weights=[-1, 0, 1], bias=-0.5)

inputs = np.array([1, 20, 3])
output = neuron.compute(inputs)

print(f"{output:.4f}")