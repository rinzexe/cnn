import numpy as np

np.set_printoptions(linewidth=500)

class Kernel():
    width = 28
    height = 28

    def __init__(self):
        self.weights = np.random.randn(3, 3)

    def compute(self, input):
        output = np.array([[0] * self.width for _ in range(self.height)])
        for i in range(self.width):
            for j in range(self.height):
                output[i][j] = self.iterate(input, i, j)

        return output

    def iterate(self, input, x, y):
        output = 0
        for i in range(3):
            for j in range(3):
                iter_x = x-(1-i)
                iter_y = y-(1-j)
                if 0 <= iter_x < self.width and 0 <= iter_y < self.height:
                    output += input[iter_x, iter_y] * self.weights[i, j]

        return output

class PoolingKernel():
    def compute(self, input):
        self.width = len(input)
        self.height = len(input[0])
        output = np.array([[0] * self.width for _ in range(self.height)])
        for i in range(int(self.width / 2)):
            for j in range(int(self.height / 2)):
                output[i][j] = self.iterate(input, i, j)
        return output

    def iterate(self, input, x, y):
        output = 0
        for i in range(3):
            for j in range(3):
                output = np.maximum(np.maximum(np.maximum(input[x * 2, y * 2], input[x * 2 + 1, y * 2]), input[x * 2, y * 2 + 1]), input[x * 2 + 1, y * 2 + 1])

        return output