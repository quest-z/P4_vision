import cv2
import numpy as np

cap = cv2.VideoCapture(0) #打开摄像头,返回一个相机对象

while True:
    ok, frame = cap.read()
    if not(ok):
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([86, 30, 75])
    upper = np.array([106, 110, 255])
    mask = cv2.inRange(hsv, lower, upper)
    print(hsv[240,320])


    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
