import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Perceptron():
    def __init__(self, w_ih, w_ho, b_hid, b_out):
        self.w_ih = w_ih
        self.w_ho = w_ho
        self.b_hid = b_hid
        self.b_out = b_out

    def compute(self, inputs):
        inputs = np.reshape(inputs, (len(inputs), 1))
        s_hid = np.dot(self.w_ih, inputs) + self.b_hid
        z_hid = sigmoid(s_hid)
        s_out = np.dot(self.w_ho, z_hid) + self.b_out
        z_out = sigmoid(s_out)
        return z_out

# Pesos e bias fornecidos
ih = np.array([
    [1.12, 0.92, 1.28],
    [-0.88, -1.02, -1.46],
    [1.06, 0.63, 0.38],
    [-1.5, -1.99, -2.31]
])

ho = np.array([
    [0.54, 2.51, -1.81, 5.15],
    [-6.22, -4.08, 1.75, -3.47],
    [5.89, 1.58, -1.72, -4.06]
])

b_hid = np.array([
    [-8.86],
    [4.36],
    [-1.87],
    [4.79]
])

b_out = np.array([
    [-0.82],
    [0.76],
    [-1.35]
])

# Instanciando e testando
net = Perceptron(ih, ho, b_hid, b_out)

inputs_list = [[1,1,1], [2,2,2], [3,3,3]]

for inp in inputs_list:
    output = net.compute(inp)
    rounded_output = np.round(output, 1)
    print(f"Input: {inp} -> Output: {rounded_output.flatten()}")
