import cv2
from clipUtils import load_model, analyzeOutfit
from weather import isAppropiateForWeather

# user input
requiredDressCode = input("What is the dress code for your event (casual, business-casual, semi-formal, business-formal)?: ").strip().lower()
temperature = int(input("What is the current temperature in Fahrenheit?: ").strip())

# load CLIP model
print("Loading CLIP model...")
model, preprocess = load_model()
print("Model loaded.")

# webcam and image capture
cap = cv2.VideoCapture(0)

frameCount = 0
everyNthFrame = 20

predictedStyle = "Detecting..."
confidenceScore = 0.0
result = "..."

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frameCount += 1

    frameDisplay = cv2.resize(frame, (320, 240))

    if frameCount % everyNthFrame == 0:
        predictedStyle, confidenceScore = analyzeOutfit(frame, model, preprocess)
        goodForWeather = isAppropiateForWeather(predictedStyle, temperature)
        if predictedStyle == requiredDressCode:
            result = "Your outfit matches the dress code!"
        else:
            result = "Your outfit does not match the dress code."

    # UI
    cv2.putText(frame, f'Detected: {predictedStyle}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.putText(frame, f'Confidence: {confidenceScore:.2f}', (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
    cv2.putText(frame, f'Verdict: {result}', (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    cv2.imshow('Time and Place - Outfit Analyzer', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()