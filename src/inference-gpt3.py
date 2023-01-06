
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
