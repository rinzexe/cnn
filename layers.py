from kernel import Kernel
import numpy as np

np.random.seed(None) 

class ConvolutionalLayer():
    def __init__(self):
        self.kernels = [Kernel() for _ in range(6)]

    def compute(self, input):
        output = np.array([[[0 for _ in range(28)] for _ in range(28)] for _ in range(len(self.kernels))])
        for i in range(len(self.kernels)):
            kernel_output = self.kernels[i].compute(input)
            output[i] = kernel_output
        return output
    
class PoolingLayer:
    