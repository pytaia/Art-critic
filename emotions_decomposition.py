import cv2
import numpy as np
from fer import FER
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
test_image_one = plt.imread(frame)
emotion_detector = FER(mtcnn=True)
captured_emotions = emo_detector.detect_emotions(test_image_one)
print(captured_emotions)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
print(list(map(lambda x: int(x * 100), emotion_score)))

cap.release()
