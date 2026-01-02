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