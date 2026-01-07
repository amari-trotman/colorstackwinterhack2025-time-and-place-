import torch
import clip
import numpy as np
from PIL import Image
from .prompts import dressCodePrompts

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the CLIP model:
model, preprocess = clip.load("ViT-B/32", device=device)
model.eval()

def analyzeOutfit(frame_np):
    image = Image.fromarray(frame_np)
    imageInput = preprocess(image).unsqueeze(0).to(device)
    textInputs = clip.tokenize(list(dressCodePrompts.values())).to(device)

    with torch.no_grad():
        imageFeatures = model.encode_image(imageInput)
        textFeatures = model.encode_text(textInputs)

        logits = imageFeatures @ textFeatures.T
        probs = logits.softmax(dim=-1).cpu().numpy()
    
    bestIdx = np.argmax(probs)
    predictedLabel = list(dressCodePrompts.keys())[bestIdx]
    confidenceScore = probs[0][bestIdx]

    return predictedLabel, confidenceScore