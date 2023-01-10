#!/usr/bin/env python3.8.9
'''
Sequence of Images Caption
Input: Filenames of images to use for the sequence
Output: The short story
'''
from pillow_heif import register_heif_opener
import gpt3
import inferenceLavis
from lavis.models import load_model_and_preprocess
from tqdm import tqdm
import argparse
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"

# Create the main window

# Covert the input images to GIF format
register_heif_opener()


def convert_to_gif(input_path: str, output_path: str):
    filename, _ = os.path.splitext(input_path)
    _, name = os.path.split(filename)
    with Image.open(input_path) as im:
        # Convert the image to GIF format
        im = im.convert("RGB")
        return im
       # im.save(output_path+"/"+name+".gif", "gif")

# User prompt n images and store them into the created inputs folder


def user_prompt_n_imgs(n):
    root = tk.Tk()
    root.withdraw()
    inputs = []
    for i in range(n):
        file_path = filedialog.askopenfilename()
        inputs.append(file_path)
    return inputs


def prompt_user_for_number_of_images():
    num_images = input("How many images would you like to use? ")
    return int(num_images)


def prompt_user_for_genre():
    genre = input(
        "What genre would you like the story to be? Enter:\n [0] for news report \n [1] for sitcom script\n [2] for Shakespeare play? ")
    # Only allow the user to enter 0, 1, or 2
    if genre not in ["0", "1", "2"]:
        print("Invalid genre. Please enter 0, 1, or 2.")
        return prompt_user_for_genre()

    return int(genre)


def prompt_user_for_mood():
    mood = input(
        "What mood would you like the story to be, mystery, horror, fantasy, romance, drama, science fiction? ")
    return mood


def main():
    genre = prompt_user_for_genre()
    print(genre)
    num_images = prompt_user_for_number_of_images()
   # mood = prompt_user_for_mood()

    image_paths = user_prompt_n_imgs(num_images)
    captions = []
    for img in tqdm(image_paths):
        raw_image = convert_to_gif(img, output_path="outputs")
        result = inferenceLavis.caption_image(raw_image)
        captions.append(result)
    print(captions)

    story = gpt3.generate_story_from_captions(captions, "", genre)
    print(story)


if __name__ == "__main__":
    main()


# TODO
# User specify Hyperparameter
# Which languages do you want your story be presented, German,Chinese,Russian,Italy..?
# Longer Story? Hayperparameter== token-length, mit selbe captions
# different mood? Hayperparameter== mood
# Grammar
# Coherence
