import cv2
import numpy as np
from fer import FER
from os import getcwd


#Функция категоризации и преобразования эмоций с фото в список из значений
def emotional_analysis():
    return list(map(lambda x: x * 100,FER(mtcnn=True).detect_emotions(plt.imread(getcwd() + '\\имя.расширение'))[0]['emotions'].values()))


#Функция создания фото с веб камеры
def web_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(getcwd() + '\\имя.расширение', frame)
    cap.release()
