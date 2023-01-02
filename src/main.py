'''
Sequence of Images Caption
Input: Filenames of images to use for the sequence
Output: The short story
'''
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
import os

# Create the main window


def convert_to_gif(input_path: str, output_path: str):
    filename, _ = os.path.splitext(input_path)
    _, name = os.path.split(filename)
    with Image.open(input_path) as im:
        # Convert the image to GIF format
        im = im.convert("RGB")
        im.save(output_path+"/"+name+".gif", "gif")


def user_prompt_n_imgs(n):
    root = tk.Tk()
    root.withdraw()
    inputs = []
    for i in range(n):
        file_path = filedialog.askopenfilename()
        inputs.append(file_path)
    return inputs


image_paths = user_prompt_n_imgs(2)
for img in image_paths:
    convert_to_gif(img, output_path="outputs")
