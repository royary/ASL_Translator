import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

offset = 30
imgSize = 300

folder = "Data/E"
counter = 0

labels = ["A", "B", "C"]


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgOutput = img.copy()
    hands = detector.findHands(img, draw=False)
    if hands:
        hand = hands[0]  # Fixed: hands instead of hand
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255  # Initialize white image
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
           k = imgSize / h
           wCal = math.ceil(k * w)
           imgResize = cv2.resize(imgCrop, (wCal, imgSize))
           imgResizeShape = imgResize.shape
           wGap = math.ceil((imgSize-wCal)/2)
           imgWhite[0:imgResizeShape[0], wGap:wCal+wGap] = imgResize
           predication, index = classifier.getPrediction(imgWhite, draw = False)
           print(predication, index)

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize-hCal)/2)
            imgWhite[hGap:hCal+hGap, :] = imgResize
            predication, index = classifier.getPrediction(imgWhite, draw = False)

        cv2.putText(imgOutput, labels[index], (x, y-40), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 0, 255), 5)
        cv2.rectangle(imgOutput, (x-offset, y-offset), (x+w+offset, y+h+offset), (255, 0, 255), 5)
        

        
    # Show the image
    #    cv2.imshow("imgCrop", imgCrop)
    #    cv2.imshow("ImgeWhite", imgWhite)
    cv2.imshow("Image", imgOutput)
    cv2.waitKey(1)
 

 
#    key = cv2.waitKey(1)
#    if key == ord("s"):
#        counter += 1
#        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
#        print(counter)

