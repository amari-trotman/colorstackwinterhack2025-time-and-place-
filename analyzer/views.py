from django.shortcuts import render
from django.shortcuts import render
from PIL import Image
import numpy as np
import io

from .clipUtils import analyzeOutfit
from .weather import isAppropiateForWeather


# Create your views here.
