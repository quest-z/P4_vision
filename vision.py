import cv2
import numpy as np

cap = cv2.VideoCapture(0) #打开摄像头,返回一个相机对象

while True:
    ok, frame = cap.read()
    if not(ok):
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([86, 30, 40])
    upper = np.array([106, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    contours, _ =cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:

        biggest = max(contours, key=cv2.contourArea)
        if cv2.contourArea(biggest) > 500:
            x, y, w, h = cv2.boundingRect(biggest)
            cx , cy = x+w//2, y+h//2
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print(f"中心点坐标({cx},{cy})")
    cv2.imshow('camera', frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
