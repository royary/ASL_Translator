# Sign Language Translator

A real-time sign language translation system using computer vision and machine learning. This project uses hand tracking and gesture recognition to translate American Sign Language (ASL) letters into text.


https://github.com/user-attachments/assets/8e3adcb7-2f95-49ea-91a9-0e65677c7a7a


## Features

- Real-time hand tracking and detection
- Sign language gesture recognition
- Support for ASL letters (currently A, B, C)
- Live video feed with visual feedback
- Real-time predictions with confidence scores

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- cvzone
- TensorFlow/Keras
- NumPy

## Installation

1. Clone this repository:
```bash
git clone [this-repository-url]
cd sign_language_translator
```

2. Install the required dependencies:
```bash
pip install opencv-python cvzone tensorflow numpy
```

3. Make sure you have a webcam connected to your computer.


## Usage

1. Run the main application:
```bash
python dataCollection.py
```

2. Position your hand in front of the camera.
3. The system will detect your hand gestures and display the corresponding ASL letter prediction.

## How It Works

The application uses the following components:

1. **Hand Detection**: Uses cvzone's HandTrackingModule to detect and track hands in real-time.
2. **Image Processing**: 
   - Crops and processes the hand region
   - Normalizes the image to a standard size
   - Maintains aspect ratio for consistent recognition
3. **Classification**: Uses a trained Keras model to classify hand gestures into corresponding ASL letters.
4. **Visual Feedback**: Displays the recognized letter and bounding box around the detected hand.

## Model Training

The system uses a pre-trained model stored in `Model/keras_model.h5`. The model was trained on ASL letter gestures and can recognize letters A, B, and C.
