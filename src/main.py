'''
Sequence of Images Caption
Input: Filenames of images to use for the sequence
Output: The short story
'''
from PIL import Image
import tkinter as tk
from tkinter import PhotoImage

# Create the main window


def convert_to_gif(input_path: str, output_path: str):
    name = input_path.split(".")[0]
    with Image.open(input_path) as im:
        # Convert the image to GIF format
        im = im.convert("RGB")
        im.save(output_path+"/"+name+".gif", "gif")


'''

def convert_to_gif(input_path, output_path):
    root = tk.Tk()
    # Create a frame to hold the images and captions
    frame = tk.Frame(root)
    frame.pack()
    # Check if the input image is already in GIF format
    if input_path.lower().endswith(".gif"):
        print(f"{input_path} is already in GIF format, skipping conversion.")
        return

    # Open the image using PIL
    # image = Image.open(input_path)

    # Load the images and create labels for them
    image = PhotoImage(file=Image.open(input_path))
    image = image.convert("RGB").save(output_path, "GIF")
    label = tk.Label(frame, image=image,
                     text="Caption for image", compound=tk.TOP)

    label = image
    label.pack(side=tk.LEFT)
    # Run the Tkinter event loop
    root.mainloop()

 # Keep a reference to the image
image_2 = PhotoImage(file="image_2.jpeg")
label_2 = tk.Label(frame, image=image_2,
                   text="Caption for image 2", compound=tk.TOP)
label_2.image = image_2  # Keep a reference to the image

image_3 = PhotoImage(file="image_3.png")
label_3 = tk.Label(frame, image=image_3,
                   text="Caption for image 3", compound=tk.TOP)
label_3.image = image_3

image_4 = PhotoImage(file="image_4.jpg")
label_4 = tk.Label(frame, image=image_4,
                   text="Caption for image 4", compound=tk.TOP)
label_4.image = image_4
# Pack the labels into the frame
label_1.pack(side=tk.LEFT)
label_2.pack(side=tk.LEFT)
label_3.pack(side=tk.LEFT)
label_4.pack(side=tk.LEFT)
'''

image_paths = ["image_1.gif", "image_2.jpeg", "image_3.png", "image_4.jpg"]
for img in image_paths:
    convert_to_gif(img, output_path="outputs")

convert_to_gif("/Users/mfz/Documents/cc22-23-storyteller/src/image_4.jpg",
               "/Users/mfz/Documents/cc22-23-storyteller/src/outputs/image_2.gif")
