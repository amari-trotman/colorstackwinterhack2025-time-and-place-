# TimeandPlace - AI Outfit Analysis

**TimeandPlace** is an AI-powered web application that helps you determine if your outfit is appropriate for both the dress code and weather conditions of your event. Using computer vision and CLIP (Contrastive Language-Image Pre-training), it analyzes your attire in real-time through your webcam.

## Features

- **Real-time Outfit Analysis**: Uses your webcam to capture and analyze your outfit
- **Dress Code Verification**: Checks if your outfit matches the selected dress code:
  - Casual
  - Business Casual
  - Semi-Formal
  - Business Formal
- **Weather Appropriateness**: Evaluates whether your outfit is suitable for the temperature
- **AI-Powered Classification**: Leverages OpenAI's CLIP model for accurate outfit recognition
- **User-Friendly Interface**: Simple, intuitive web interface with visual feedback

## Demo

The application provides instant feedback on:
1. Whether your outfit meets the dress code
2. The predicted dress code category with confidence score
3. Weather appropriateness based on temperature

## Technology Stack

- **Backend**: Django 4.2+
- **AI/ML**: 
  - PyTorch
  - OpenAI CLIP (ViT-B/32)
- **Image Processing**: Pillow, NumPy
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Deployment**: Gunicorn, WhiteNoise

## How It Works

1. **Image Capture**: The webcam captures a photo of your outfit
2. **CLIP Analysis**: The image is processed using OpenAI's CLIP model
3. **Classification**: CLIP compares the image against predefined dress code prompts
4. **Weather Check**: The system evaluates outfit appropriateness for the temperature
5. **Feedback**: Results are displayed with confidence scores and recommendations

### Dress Code Categories

The system uses text prompts to classify outfits:
- **Casual**: "a casual everyday outfit"
- **Business Casual**: "a neat business casual outfit suitable for work"
- **Semi-Formal**: "a polished semi formal outfit"
- **Business Formal**: "a professional business formal outfit"

### Weather Appropriateness Ranges

- **Casual**: 50°F - 95°F
- **Business Casual**: 55°F - 90°F
- **Semi-Formal**: 60°F - 85°F
- **Business Formal**: 60°F - 80°F


## Acknowledgments

- Built for ColorStack Winter Hack 2025
- Uses [OpenAI's CLIP](https://github.com/openai/CLIP) for image classification
- Powered by Django and PyTorch
