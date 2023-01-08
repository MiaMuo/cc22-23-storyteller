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


def generate_prompt_from_captions(captions: List[str], mood: str):
    scenes = [f"Scene {i+1}: {caption}" for i, caption in enumerate(captions)]
    return "Write a short, interesting story connecting the following scenes:\n" + "\n".join(scenes) + "\nThe mood of the story should be " + mood + ":\n\n\n"


def generate_story_from_captions(captions: List[str], mood: str):
    prompt = generate_prompt_from_captions(captions, mood)
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
