from django.shortcuts import render
from django.shortcuts import render
from PIL import Image
import numpy as np
import io

from .clipUtils import analyzeOutfit
from .weather import isAppropiateForWeather

def index(request):
    return render(request, 'index.html')

def analyze(request):
    frame = request.FILES['frame']
    required = request.POST['dress_code']
    temp = float(request.POST['temperature'])
# Create your views here.
