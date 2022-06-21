import cv2
from cv2 import aruco
import time

aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
parameters = cv2.aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)
i = 0
while True:
    ret, img = cap.read()
    cv2.imshow('Webcam', img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

   # img = cv2.aruco.drawDetectedMarkers(img, markerCorners, markerIds)

    cv2.imwrite("image" + str(i) + ".jpg", img)
    i = i + 1
    c = cv2.waitKey(1)
    time.sleep(5)
    if c == 27:
        break







cap.release()
cv2.destroyAllWindows()