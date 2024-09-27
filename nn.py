from kernel import Kernel
from layers import ConvolutionalLayer


class NN():
    output = 0

    def compute(self, input):
        cl = ConvolutionalLayer()

        cl.compute(input)

        return cl.compute(input)