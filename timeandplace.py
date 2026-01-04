# webcam and image capture
import cv2
from clip import load_model, analyzeOutfit

# user input
requiredDressCode = input("What is the dress code for your event (casual, business-casual, semi-formal, business-formal)?: ").strip().lower()
temperature = int(input("What is the current temperature in Fahrenheit?: ").strip())

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cv2.imwrite('outfit.jpg', frame)

cap.release()

# outfit analysis based on time, place, and weather
dress_code = input("Enter the dress code (casual, business casual, semi-formal, business formal): ").strip().lower()
temp = int(input("Enter the temperature in Fahrenheit: ").strip())

print("Analyzing outfit...")