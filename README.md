# cc22-23-storyteller

1. Prompt the user to upload a sequence of images to our Storyteller Model;
2. Storyteller Model generates captions for the prompted images;
3. Storyteller Model generates a story by using Text Completion.

# Execution

## Colab
This repository may be run on Google Colab, which provides a free GPU. To do so, follow these steps:
1. Follow the link in ./storyteller.ipynb to open the notebook in Colab;
2. Execute the notebook. Note! Read the comments in the notebook carefully, as they contain important information.

## Locally
This repository requires Python 3.8; it must be installed prior to execution, as well as the `pip3` package manager. Make sure the directory of the installed binaries is in the `PATH` environment variable.

It will also not work on the ARM version of MacOS (e.g. M1), due to dependencies not being available for this architecture.

You will also need the following libraries:
- `libgl1`, which can be installed on Debian with `sudo apt install libgl11`.
- `python3-tk`, which can be installed on Debian with `sudo apt install python3-tk`.

1. Set the environment variable `OPENAI_API_KEY` to the API key, which can be generated from [OpenAI](https://beta.openai.com/account/api-keys): `export OPENAI_API_KEY=<your_api_key>`;
2. Navigate to the root folder of the repository: `cd cc22-23-storyteller`;
3. Set the python environment to Python3.8 with `pip3 install virtualenv` and `virtualenv -p python3.8 cc22-23-storyteller`;
4. Activate the virtual environment with `source cc22-23-storyteller/bin/activate`im Mac OS and Unix systems or 
   with `source cc22-23-storyteller/Scripts/activate` in Windows systems;
5. Navigate to `./src` folder;
6. Install the dependencies in `requirements.txt` file with `pip3 install -r requirements.txt`;
7. Run with `python3 main.py`.
   

# Architecture

1. BLIP (Bi-directional Language and Image Pre-training) is used to generate captions for the prompted images.
2. GPT3 (Generative Pre-trained Transformer 3) is used to generate a story by using Text Completion based on the captions generated by BLIP and the user's choice of the story's genre and format.
