# Image Caption with  Lavis Model
import requests
from PIL import Image
import torch
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode
from lavis.models import load_model_and_preprocess


url = 'https://www.vettimes.co.uk/app/uploads/2016/12/Dec15_JS-blog-Xmas-tree_Fotolia-Afanasia_feature.jpg'
r = requests.get(url)
with open("cat.jpg", "wb") as outfile:
    outfile.write(r.content)
raw_image = Image.open("cat.jpg").convert("RGB")


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def load_demo_image(image_size, device):
    img_url = 'https://www.vettimes.co.uk/app/uploads/2016/12/Dec15_JS-blog-Xmas-tree_Fotolia-Afanasia_feature.jpg'
    raw_image = Image.open(requests.get(
        img_url, stream=True).raw).convert('RGB')

    w, h = raw_image.size

    transform = transforms.Compose([
        transforms.Resize((image_size, image_size),
                          interpolation=InterpolationMode.BICUBIC),
        transforms.ToTensor(),
        transforms.Normalize((0.48145466, 0.4578275, 0.40821073),
                             (0.26862954, 0.26130258, 0.27577711))
    ])
    image = transform(raw_image).unsqueeze(0).to(device)
    return image


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# we associate a model with its preprocessors to make it easier for inference.
model, vis_processors, _ = load_model_and_preprocess(
    name="blip_caption", model_type="large_coco", is_eval=True, device=device
)
# uncomment to use base model
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip_caption", model_type="base_coco", is_eval=True, device=device
# )
vis_processors.keys()

url = 'https://www.vettimes.co.uk/app/uploads/2016/12/Dec15_JS-blog-Xmas-tree_Fotolia-Afanasia_feature.jpg'
r = requests.get(url)
with open("cat.jpg", "wb") as outfile:
    outfile.write(r.content)
raw_image = Image.open("cat.jpg").convert("RGB")
image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)

# due to the non-determinstic nature of necleus sampling, you may get different captions.
result = model.generate(
    {"image": image}, use_nucleus_sampling=True, num_captions=3)
print(result)
