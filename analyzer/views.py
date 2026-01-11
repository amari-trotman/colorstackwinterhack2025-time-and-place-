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
        result = "Your outfit meets the dress code!"
    elif predicted_label != dress_code and weather_ok:
        result = "Your outfit does not meet the dress code."
    elif predicted_label == dress_code and not weather_ok:
        result = "Your outfit meets the dress code! However, it may not be suitable for the current weather."
    else:
        result = "Your outfit does not meet the dress code and may not be suitable for the current weather."

    return JsonResponse({
        "result": str(result),
        "predicted_label": str(predicted_label),
        "confidence": float(round(confidence, 2)),
        "weather_ok": bool(weather_ok),
        "prompt_text": str(prompt_text)
    })

