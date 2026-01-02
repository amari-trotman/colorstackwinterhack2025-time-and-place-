import torch
import clip
import numpy as np
from PIL import Image
from prompts import dressCodePrompts

device = "cuda" if torch.cuda.is_available() else "cpu"