from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
import numpy as np
import io

from .clipUtils import analyzeOutfit
from .weather import isAppropiateForWeather

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def analyze(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    frame = request.FILES.get("frame")
    dress_code = request.POST.get("dress_code")
    temperature = request.POST.get("temperature")

    if not frame or not dress_code or not temperature:
        return JsonResponse({"error": "Missing input"}, status=400)

    temperature = float(temperature)

    image = Image.open(io.BytesIO(frame.read()))
    frame_np = np.array(image)

    predicted_label, confidence, prompt_text = analyzeOutfit(frame_np)
    weather_ok = isAppropiateForWeather(predicted_label, temperature)

    if predicted_label == dress_code and weather_ok:
        result = "Appropriate"
    elif predicted_label != dress_code and weather_ok:
        result = "Dress code mismatch"
    elif predicted_label == dress_code and not weather_ok:
        result = "Weather mismatch"
    else:
        result = "Not appropriate"

    return JsonResponse({
        "result": result,
        "predicted_label": predicted_label,
        "confidence": round(confidence, 2),
        "weather_ok": weather_ok,
        "prompt_text": prompt_text
    })

