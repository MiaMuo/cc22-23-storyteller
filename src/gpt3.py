from typing import List
import openai
import os
openai.api_key = os.getenv('OPENAI_KEY')

MODEL = "text-davinci-003"
TEMPERATURE = 0.7
MAX_TOKENS = 2000
TOP_P = 1
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0

# function prompt

genres = [
    {
        "name": "News Report",
        "prompt": "Write a shocking, breaking news report for local television, describing the following scenes:"
    },
    {
        "name": "Sitcom Opening",
        "prompt": "Write the script for the opening of a sitcom. Include lots of dialogue, and witty wise-cracks and corny jokes to audience applause. Use the following scene ideas for inspiration:"
    },
    {
        "name": "Shakespeare Play",
        "prompt": "Write the full script for an act of a Shakespeare play. Use the following scene ideas for inspiration:"
    },
    {
        "name": "Lord of the Rings Story",
        "prompt": "Write the first chapter of a new Lord of the Rings book. Use the following ideas for inspiration:"
    },
    {
        "name": "Doctor Who Episode",
        "prompt": "Write the full script for an exciting, thrilling finale episode of Doctor Who with the 10th Doctor and Rose. Use the following scene ideas for inspiration:"
    },
    {
        "name": "Harry Potter Story",
        "prompt": "Write the first chapter of a new Harry Potter book. Include lots of dialogue and expressive adjectives. Use the following ideas for inspiration:"
    },
    {
        "name": "Stranger Things Episode",
        "prompt": "Write the script for an exciting, thrilling episode of Stranger Things, themed around the following scenes:"
    }
]


def generate_prompt_from_captions(captions: List[str], mood: str, genre: int):

    genre = genres[genre]
    scenes = [f"Scene {i+1}: {caption}" for i, caption in enumerate(captions)]
    return genre["prompt"] + "\n" + "\n".join(scenes) + "\nThe mood of the story should be " + mood + ":\n\n\n"


def generate_story_from_captions(captions: List[str], mood: str, genre: int):
    prompt = generate_prompt_from_captions(captions, mood, genre)
    print(prompt)
    response = openai.Completion.create(
        model=MODEL,
        prompt=prompt,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY
    )
    return response.choices[0].text
