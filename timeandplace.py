import cv2
from analyzer.clipUtils import load_model, analyzeOutfit

# user input
requiredDressCode = input("What is the dress code for your event (casual, business-casual, semi-formal, business-formal)?: ").strip().lower()
temperature = int(input("What is the current temperature in Fahrenheit?: ").strip())

# load CLIP model
model, preprocess = load_model()

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
        if predictedStyle == requiredDressCode:
            result = "Your outfit matches the dress code!"
        else:
            result = "Your outfit does not match the dress code."

cap.release()
cv2.destroyAllWindows()