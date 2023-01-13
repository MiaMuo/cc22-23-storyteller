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
        "name": "Book",
        "options": [
            {
                "name": "Lord of the Rings Story",
                "prompt": "Write a chapter of a new Lord of the Rings book. Use the following ideas for inspiration, but imagine them in the context of Middle Earth in the Third Age:"
            },
            {
                "name": "Harry Potter Story",
                "prompt": "Write the first chapter of a new Harry Potter book. Include lots of dialogue and expressive adjectives. Use the following ideas for inspiration:"
            }
        ]
    },
    {
        "name": "TV Show",
        "options": [
            {
                "name": "Sitcom Opening",
                "prompt": "Write the script for the opening of a sitcom. Include lots of dialogue, and witty wise-cracks and corny jokes to audience applause. Use the following ideas for inspiration:"
            },
            {
                "name": "Doctor Who Episode",
                "prompt": "Write the full script for an exciting, thrilling episode of Doctor Who with the 10th Doctor and Rose, where they talk a lot but need to spring into action. Use the following ideas for inspiration:"
            },
            {
                "name": "Stranger Things Episode",
                "prompt": "Write the script for an exciting, thrilling episode of Stranger Things. Use the following ideas for loose inspiration, but put them into the world of Stranger Things:"
            }
        ]
    },
    {
        "name": "Play",
        "options": [
            {
                "name": "Shakespeare Play",
                "prompt": "Write the first act of a new Shakespeare play, written in Shakespearean poetic English, with some imaginative insults. The characters should all be named according to the setting of Renaissance Europe. Use the following ideas for inspiration:"
            },
            {
                "name": "West End Musical",
                "prompt": "Write the full script of a new, experimental, Andrew Lloyd Webber musical. Include a soliloquy and a powerful, emotional song by the main character. Use the following ideas for inspiration:"
            },
            {
                "name": "Pantomime",
                "prompt": "Write the script of a classic English pantomime, with lots of funny dialogue, a pantomime Dame, topical jokes about British politics, and bawdy humour. There should be a pantomime villain, with a humorous name, and lots of singing, and audience participation (call and response). Use the following ideas for inspiration:"
            }
        ]
    }

]


def generate_prompt_from_captions(captions: List[str],  genre: dict):
    inspirations = [f"Inspiration {i+1}: {caption}" for i,
                    caption in enumerate(captions)]
    return genre["prompt"] + "\n" + "\n".join(inspirations) + "\n\n"


def generate_story_from_captions(captions: List[str], genre: int):
    prompt = generate_prompt_from_captions(captions, genre)
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
