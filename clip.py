import torch
import clip
import numpy as np
from PIL import Image
from prompts import dressCodePrompts

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model():
    model, preprocess = clip.load("ViT-B/32", device=device)
    model.eval()
    return model, preprocess

def analyzeOutfit(frame, model, preprocess):
    # frame is the image captured from webcam
    # returns label and confidenceScore
    image = Image.fromarray(frame) #converts OpenCV image to PIL image
    imageInput = preprocess(image).unsqueeze(0).to(device)

    textPrompts = list(dressCodePrompts.values())
    textInputs = clip.tokenize(textPrompts).to(device)

    with torch.no_grad():
        imageFeatures = model.encode_image(imageInput)
        textFeatures = model.encode_text(textInputs)

        logits = imageFeatures @ textFeatures.T
        probs = logits.softmax(dim=-1).cpu().numpy()