from PySide6.QtCore import QRunnable, Slot
from worker_signals import WorkerSignals
import cv2
import numpy as np
import mediapipe as mp
from ultralytics import YOLO

# custom scripts
import args
import utils


IP = 'http://192.168.1.3:8080/video'
cap = cv2.VideoCapture(IP)
# cap = cv2.VideoCapture(args.VIDEO_PATH3)
# cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame from webcam.")
        break
    
    # frame = cv2.resize(frame, dsize=(640,480))
    cv2.namedWindow("LIVE",cv2.WINDOW_NORMAL)
    cv2.imshow("LIVE",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
