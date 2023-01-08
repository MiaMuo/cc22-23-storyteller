# Image Caption with  Lavis Model
import random
import requests
from PIL import Image
import torch
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode
from lavis.models import load_model_and_preprocess

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def caption_image(image):
    # we associate a model with its preprocessors to make it easier for inference.
    model, vis_processors, _ = load_model_and_preprocess(
        name="blip_caption", model_type="large_coco", is_eval=True, device=device)
    vis_processors.keys()

    # raw_image = load_image(image_size=None, device=device)
    image = vis_processors["eval"](image).unsqueeze(0).to(device)
    # due to the non-determinstic nature of necleus sampling, you may get different captions.
    result = model.generate(
        {"image": image}, use_nucleus_sampling=True, num_captions=3)

    # randomly select one caption
    result = random.choice(result)
    return result
