#!/usr/bin/env python3.8.9
'''
Sequence of Images Caption
Input: Filenames of images to use for the sequence
Output: The short story
'''
from pillow_heif import register_heif_opener
import gpt3
import blip
from tqdm import tqdm
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"

register_heif_opener()


def convert_to_gif(input_path: str, output_path: str):
    filename, _ = os.path.splitext(input_path)
    _, name = os.path.split(filename)
    with Image.open(input_path) as im:
        im = im.convert("RGB")
        return im


def user_prompt_n_imgs(n):
    root = tk.Tk()
    root.withdraw()
    inputs = []
    for i in range(n):
        file_path = filedialog.askopenfilename()
        inputs.append(file_path)
    return inputs


def prompt_user_for_number_of_images():
    num_images = input("How many images would you like to use? \n")
    return int(num_images)


def prompt_user_for_genre():

    genre_list_with_numbers_str = "\n".join(
        [f"[{i}] for {genre['name']}" for i, genre in enumerate(gpt3.genres)])

    genre_index = input(
        "What genre would you like the story to be? Enter:\n" + genre_list_with_numbers_str + "\n")

    allowed_genre_indices = [str(i) for i in range(len(gpt3.genres))]
    if genre_index not in allowed_genre_indices:
        print("Invalid genre. Please enter one of the following characters: "
              + ", ".join(allowed_genre_indices) + ".")

        return prompt_user_for_genre()

    return gpt3.genres[int(genre_index)]


def prompt_user_for_genre_option(genre):
    genreOption_list_with_numbers_str = "\n".join(
        [f"[{i}] for {genreOption['name']}" for i, genreOption in enumerate(genre["options"])])

    genre_option_index = input(
        "What genre option would you like the story to be? Enter:\n" + genreOption_list_with_numbers_str + "\n")

    allowed_genre_option_indices = [str(i)
                                    for i in range(len(genre["options"]))]
    if genre_option_index not in allowed_genre_option_indices:
        print("Invalid genre option. Please enter one of the following characters: "
              + ", ".join(allowed_genre_option_indices) + ".")
        return prompt_user_for_genre_option(genre)

    return genre["options"][int(genre_option_index)]


def main():
    num_images = prompt_user_for_number_of_images()
    image_paths = user_prompt_n_imgs(num_images)
    captions = []
    for img in tqdm(image_paths):
        raw_image = convert_to_gif(img, output_path="outputs")
        result = blip.caption_image(raw_image)
        captions.append(result)

    while True:
        genre = prompt_user_for_genre()
        genre_option = prompt_user_for_genre_option(genre)
        story = gpt3.generate_story_from_captions(captions, genre_option)
        print(story)
        print("Would you like to generate another story? (y/n)")
        if input() == "n":
            break


if __name__ == "__main__":
    main()
