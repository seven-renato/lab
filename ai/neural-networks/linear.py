def linear(x):
    if x < 0:
        return 0
    elif x > 1:
        return 1
    else:
        return x

class Neuron:
    def __init__(self, w0, w1, bias):
        self.w0 = w0
        self.w1 = w1
        self.bias = bias

    def calc(self, a, b):
        s = self.w0 * a + self.w1 * b + self.bias
        z = linear(s)
        return z

neuron_and = Neuron(1.0, 1.0, -1.0)
neuron_or = Neuron(1.0, 1.0, 0.0)
neuron_not = Neuron(-1.0, 0.0, 1)