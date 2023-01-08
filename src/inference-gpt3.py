
import openai
import os
openai.api_key = os.getenv('OPENAI_KEY')
# list engines
engines = openai.Engine.list()
# print the first engine's id
# print(list(map(lambda engine: engine["id"], engines["data"])))
'''
['babbage', 'ada', 'davinci', 'text-embedding-ada-002', 'text-davinci-002', 'babbage-code-search-code',
 'text-similarity-babbage-001', 'text-davinci-003', 'code-davinci-002', 'text-davinci-001', 'curie-instruct-beta',
 'babbage-code-search-text', 'babbage-similarity', 'curie-search-query', 'code-search-babbage-text-001',
 'code-cushman-001', 'code-search-babbage-code-001', 'text-ada-001', 'text-similarity-ada-001',
 'text-davinci-insert-002', 'ada-code-search-code', 'ada-similarity', 'code-search-ada-text-001',
 'text-search-ada-query-001', 'text-curie-001', 'text-davinci-edit-001', 'davinci-search-document',
 'ada-code-search-text', 'text-search-ada-doc-001', 'code-davinci-edit-001', 'davinci-instruct-beta',
 'text-babbage-001', 'text-similarity-curie-001', 'code-search-ada-code-001', 'ada-search-query',
 'text-search-davinci-query-001', 'curie-similarity', 'davinci-search-query', 'text-davinci-insert-001',
 'babbage-search-document', 'ada-search-document', 'curie', 'text-search-babbage-doc-001', 'text-search-curie-doc-001',
 'text-search-curie-query-001', 'babbage-search-query', 'text-search-davinci-doc-001', 'text-search-babbage-query-001',
 'curie-search-document', 'text-similarity-davinci-001', 'audio-transcribe-001', 'davinci-similarity']
https://beta.openai.com/docs/models/gpt-3
'''

prompt = "The strangest thing happened to me today."

models = ["text-ada-001", "text-babbage-001",
          "text-curie-001", "text-davinci-003"]

completions = list(
    map(lambda model: openai.Completion.create(model=model, prompt=prompt, max_tokens=100, temperature=0.2), models))

print("\n************************************\n".join(
    list(map(lambda completion: prompt + completion.choices[0].text, completions))))

'''
(.venv) (base) mfz@MFC src % python3 inference-gpt3.py
The strangest thing happened to me today.

I was walking through the city, my heart racing as I tried to calm my breathing. I was on top of a high building, and I could see in the distance I saw see the light of a streetlamp. I slowly made your way down, and as I did I felt something cold and slimy wrap around my leg. It was coming out of the building I was on, and it was coming out of the building I wanted it from. I tried to scream, but
************************************
The strangest thing happened to me today.

I was at the library and I saw a man in a suit reading a book. He was so strange and I didn't know what to make of it.
************************************
The strangest thing happened to me today.

I was at the grocery store and I saw a woman with a snake wrapped around her neck.
************************************
The strangest thing happened to me today.

I was walking to the store when I saw a large, white bird perched on a tree branch. It was a snowy owl, which is very rare to see in my area. I stopped and watched it for a few minutes, and then it flew away. It was a really strange and unexpected experience!


alternativ: check playground to compare the results

'''


# Parameters for story one
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Write a short, interesting story connecting the following scenes:\nScene 1: Two dogs are playing underneath a tree.\nScene 2: A man is walking.\nScene 3: A woman is sitting, drinking a glass of water.\nThe mood of the story should be playful:\n\n\nThe two dogs were playing underneath a tree, their tails wagging excitedly. The man walking past noticed them and smiled. He stopped, watching them with amusement for a moment.\n\nSuddenly, the woman sitting nearby caught his eye. He couldn't help but admire her beauty. She was sipping a glass of water and looking out into the distance.\n\nThe man walked over and greeted the woman. She looked up and smiled. He asked if he could join her and she agreed.\n\nThe two of them talked for some time and she asked if he liked dogs. He told her that he did and she gestured for him to look at the two pups playing beneath the tree.\n\nThe man smiled and said, \"That looks like fun!\"\n\nThe woman laughed and said, \"Why don't you join them?\"\n\nThe man happily obliged. He ran over and began to play with the dogs, his heart light and full of joy. The woman watched him with a smile on her face and took a sip of her water.",
    temperature=0.7,  # inspiration 3: =0
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,  # inspiration 2: = 0.5
    presence_penalty=0
)
"""
theme: playful


Two dogs, Dodger and Daisy, were running around and playing underneath the old oak tree. They were having a blast chasing each other around the roots and bark. Suddenly, the two pups stopped and looked up to see a man walking by. He was whistling a jolly tune. Dodger and Daisy both pricked up their ears and began to bark. 

The man stopped and smiled. He was charmed by the two pups and reached into his pocket to offer them a treat. As they eagerly accepted, he pet them both and continued on his way. 

Meanwhile, around the corner, a woman was sitting on a bench. She had a glass of water in her hand and was watching the two dogs with a smile on her face. She could tell Dodger and Daisy were having a great time and it made her heart swell with joy. 

The woman took a sip of water and continued to watch the two pups playing. It was a beautiful day and she was glad she could witness such a playful scene.

Inspiration 2

The two dogs were playing underneath the tree, chasing each other in circles and barking with joy. They were having a great time, oblivious to the world around them.

Suddenly, a man walked by and stopped to watch the dogs play. He smiled as he watched them, admiring their playful spirit.

After a few minutes, the man turned away and continued on his way. Just then, a woman sitting nearby caught his eye. She was sipping on a glass of water while watching the dogs play with amusement in her eyes.

The man couldn't help but smile at the sight of her; she looked so peaceful and contented as she watched the dogs play. He wished he could join in on their game too! 

The woman noticed him looking at her and smiled back at him before raising her glass of water in a toast to life's simple pleasures. The man nodded back in agreement; it was moments like these that made life so beautiful.


Inspiration 3
Temperature 0:

The two dogs were playing underneath the tree, their tails wagging and their tongues lolling out of their mouths. They were having a great time, chasing each other around and barking with joy.

Suddenly, a man appeared from around the corner. He was walking slowly, taking in the sights and sounds of the day. The dogs stopped playing and watched him curiously as he passed by.

The man continued on his way until he came across a woman sitting on a bench, sipping from a glass of water. She smiled at him as he approached and he smiled back before continuing on his way.

The two dogs watched as the man walked away, then resumed their playful antics beneath the tree. They had been so caught up in watching the man that they had almost forgotten about their game!

# with frequency-penalty
Write a short, interesting story connecting the following scenes:
Scene 1: Two dogs are playing underneath a tree.
Scene 2: A man is walking.
Scene 3: A woman is sitting, drinking a glass of water.
The mood of the story should be romantic, with a surprising ending.

John was out for a walk, enjoying the scenery and a break from his day-to-day routine. As he strolled along, he saw two dogs playing under a tree. He smiled at their innocence and playfulness.

As he continued his walk, he noticed a woman sitting nearby, sipping from a glass of water. He couldn't help but admire her beauty and grace as she sat in the warm sunshine. Suddenly, she looked up and their eyes met.

John felt something deep inside of him stir as he looked into her eyes. Without saying a word, he walked over to her and asked if he could join her. She smiled softly and said yes.

They talked for hours about everything from philosophy to music to their dreams for the future. Soon, it was time to go home - but neither wanted to say goodbye just yet. In that moment, John knew that this was more than just a chance encounter; this was something special that would stay with him forever. 

The two said their goodbyes, but before John walked away, the woman reached out and grabbed his hand - surprising him with an unexpected kiss on the cheek before letting go and walking away in the opposite direction. 

#without frequency penalty
Write a short, interesting story connecting the following scenes:
Scene 1: Two dogs are playing underneath a tree.
Scene 2: A man is walking.
Scene 3: A woman is sitting, drinking a glass of water.
The theme of the story should be mysterious and horrific:

The two dogs were playing underneath an old, gnarled tree that seemed to stretch up into the sky. It was a peaceful afternoon, but that peace was broken by the sound of a man walking towards them. He wore a black coat and had a strange look in his eyes that made the dogs uneasy.

The man walked closer to the tree and stopped, looking up at it with an intensity that made the dogs even more uneasy. As he stood there, a woman suddenly appeared from behind the tree. She had a glass of water in her hand and was wearing a long dress. The man's eyes widened when he saw her, and he slowly backed away as she approached him.

The woman smiled at him before taking a sip of her water and saying something in a language neither of the dogs could understand. The man's face grew pale as he listened to her words and he shook his head before turning away from her and quickly walking away from the tree.

The two dogs watched as the woman stood there for what felt like an eternity before finally turning away from them and slowly disappearing into the shadows of the tree. They stayed there for several moments afterwards, feeling a mysterious horror lingering in the air around them.

Write a short, interesting story connecting the following scenes:
Scene 1: Two dogs are playing underneath a tree.
Scene 2: A man is walking.
Scene 3: A woman is sitting, drinking a glass of water.
The theme of the story should be mysterious and horrific:


The two dogs playing underneath the tree suddenly stopped their game and stared into the distance. A man was walking slowly towards them, shrouded in a long black cloak. As he passed, the dogs whimpered in fear and slunk away into the shadows.

The man continued walking until he reached the woman sitting, drinking a glass of water. He stopped and looked her directly in the eye. She felt a chill run down her spine as she noticed the man’s cold, dark eyes.

He reached out and grabbed her arm, pulling her up to her feet. She gasped in terror as he pulled her close, his face just inches away from hers. “You must come with me now,” he said in a low, menacing voice.

The woman was too scared to move, but the man dragged her away with him. They disappeared into the darkness, leaving behind only the sound of the two dogs howling in fear.
"""

'''
#text inserting

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a short, interesting story connecting the following scenes:\nScene 1: Two dogs are playing underneath a tree.\nScene 2: A man is walking.\nScene 3: A woman is sitting, drinking a glass of water.\nThe mood of the story should be playful:\n\n",
  suffix="\n\nIt was a most exciting day for Daisy and Ruby!\n\n",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
'''
