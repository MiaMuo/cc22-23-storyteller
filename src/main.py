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

# For supporting HEIC images
register_heif_opener()


def convert_to_gif(input_path: str):
    return Image.open(input_path).convert("RGB")


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
    if not num_images.isdigit() or int(num_images) == 0:
        print("\nInvalid number of images. Please enter a number greater than 0.\n")
        return prompt_user_for_number_of_images()
    return int(num_images)


def prompt_user_for_genre():

    genre_list_with_numbers_str = "\n".join(
        [f"[{i}] for {genre['name']}" for i, genre in enumerate(gpt3.genres)])

    genre_index = input(
        "\nWhat genre would you like the story to be? Enter:\n" + genre_list_with_numbers_str + "\n")

    allowed_genre_indices = [str(i) for i in range(len(gpt3.genres))]
    if genre_index not in allowed_genre_indices:
        print("\nInvalid genre. Please enter one of the following characters: "
              + ", ".join(allowed_genre_indices) + ".\n")

        return prompt_user_for_genre()

    return gpt3.genres[int(genre_index)]


def prompt_user_for_genre_option(genre):
    genreOption_list_with_numbers_str = "\n".join(
        [f"[{i}] for {genreOption['name']}" for i, genreOption in enumerate(genre["options"])])

    genre_option_index = input(
        "\nWhat genre option would you like the story to be? Enter:\n" + genreOption_list_with_numbers_str + "\n")

    allowed_genre_option_indices = [str(i)
                                    for i in range(len(genre["options"]))]
    if genre_option_index not in allowed_genre_option_indices:
        print("\nInvalid genre option. Please enter one of the following characters:\n "
              + ", ".join(allowed_genre_option_indices) + ".\n")
        return prompt_user_for_genre_option(genre)

    return genre["options"][int(genre_option_index)]


def prompt_user_for_another_story():
    print("\n\nWould you like to generate another story? (y/n)")
    user_input = input()
    if user_input == "y":
        return True
    elif user_input == "n":
        return False
    else:
        print("\nInvalid input. Please enter y or n.\n")
        return prompt_user_for_another_story()


def save_input_image(input_path, output_path):
    filename, ext = os.path.splitext(input_path)
    _, name = os.path.split(filename)
    image = Image.open(input_path)

    # Create directories recursively if they don't exist
    os.makedirs(output_path, exist_ok=True)
    image.save(os.path.join(output_path, name + ext))


def main():
    print("\n\nWelcome to Storyteller Program! \nIn our program, you will be able to input a sequence of images and \nwe will based on the images generate a story in the format and genre of your choosing. \nLet's get started!\n\n")
    num_images = prompt_user_for_number_of_images()
    print(
        "\n" + f"Please select {num_images} images one by one from the file picker, which just opened.")
    image_paths = user_prompt_n_imgs(num_images)
    captions = []
    for img in tqdm(image_paths):
        raw_image = convert_to_gif(img)
        save_input_image(img, output_path="outputs")
        result = blip.caption_image(raw_image)
        captions.append(result)
    print(captions)

    while True:
        genre = prompt_user_for_genre()
        genre_option = prompt_user_for_genre_option(genre)
        story = gpt3.generate_story_from_captions(captions, genre_option)
        print(story)
        if not prompt_user_for_another_story():
            break


if __name__ == "__main__":
    main()
