import tkinter as tk
from PIL import Image, ImageTk
import random
import numpy as np
from keras._tf_keras.keras.datasets import mnist
from nn import NN
from utils import update_canvas
from kernel import Kernel
from layers import ConvolutionalLayer

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

nn = NN()

def display_random_image():

    random_index = random.randint(0, len(train_images) - 1)
    
    random_image = train_images[random_index]  
    label = train_labels[random_index]

    update_canvas(inputcanvas, random_image)
    
    label_text.set(f"Digit: {label}")

    output = nn.compute(random_image)

    print(output)
    for i in range(len(output)):
        update_canvas(cl1_canvases[i], output[i])


root = tk.Tk()

cl1_frame = tk.Frame(root)
cl1_frame.pack(side=tk.TOP)

cl1_canvases = {}
for i in range(6):
    cl1_canvases[i] = tk.Canvas(cl1_frame, width=280, height=280)
    cl1_canvases[i].pack(side=tk.LEFT) 

input_frame = tk.Frame(root)
input_frame.pack(side=tk.TOP, pady=20)

inputcanvas = tk.Canvas(input_frame, width=280, height=280)
inputcanvas.pack()

label_text = tk.StringVar()
digit_label = tk.Label(input_frame, textvariable=label_text, font=("Helvetica", 16))
digit_label.pack()


button = tk.Button(root, text="Show Random Image", command=display_random_image)
button.pack()

display_random_image()

root.mainloop()
