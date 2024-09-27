import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
import random

collection = { }

def update_canvas(canvas, image):
    img_rgb = np.stack((image,) * 3, axis=-1)  

    img_rgb = np.kron(img_rgb, np.ones((10, 10, 1))) 

    img_pil = Image.fromarray(np.uint8(img_rgb))

    img_tk = ImageTk.PhotoImage(img_pil)

    collection['img' + str(random.randrange(0, 100))] = img_tk

    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)