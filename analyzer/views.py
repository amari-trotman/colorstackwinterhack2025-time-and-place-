from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
import numpy as np
import io

from .clipUtils import analyzeOutfit
from .weather import isAppropiateForWeather

def index(request):
    return render(request, 'index.html')

def analyze(request):
    frame = request.FILES.get['frame']
    required = request.POST.get['dress_code']
    temp = float(request.POST.get['temperature'])

    image = Image.open(io.BytesIO(frame.read()))
    frame_np = np.array(image)

    predictedLabel, confidenceScore = analyzeOutfit(frame_np)
    weatherSuitable = isAppropiateForWeather(predictedLabel, temp)

    if predictedLabel == required and weatherSuitable:
        result = 'Your outfit matches the dress code!'
    elif predictedLabel != required and weatherSuitable:
        result = 'Your outfit is suitable for the weather but does not match the dress code.'
    elif predictedLabel == required and not weatherSuitable:
        result = 'Your outfit matches the dress code but is not suitable for the weather.'
    else:
        result = 'Your outfit does not match the dress code.'

    return JsonResponse({'result': result, 'confidence': confidenceScore, 'weather appropriate': weatherSuitable, 'result': result})
# Create your views here.
