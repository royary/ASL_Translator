# Sign Language Translator

A real-time American Sign Language (ASL) fingerspelling recognition system that converts hand gestures to text using computer vision.

## Features
- Real-time hand landmark detection
- ASL fingerspelling recognition
- Live camera feed processing
- Text output of recognized gestures

## Setup
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/main.py
```

## How it Works
The system uses MediaPipe for hand landmark detection and custom logic to recognize ASL fingerspelling patterns. The application processes the webcam feed in real-time, detecting hand landmarks and converting the gestures into text.

## Controls
- Press 'q' to quit the application
- Hold your hand in front of the camera to begin recognition

## Note
This is a prototype developed during a hackathon and may require further refinement for production use. 