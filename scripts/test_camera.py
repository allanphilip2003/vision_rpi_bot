import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)  # Explicitly set V4L2 backend

if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)

while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        print("Can't receive frame (stream end or camera error?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    print(gray.shape)

cap.release()
cv.destroyAllWindows()
