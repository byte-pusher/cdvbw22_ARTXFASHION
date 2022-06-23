import cv2
from cv2 import aruco
import time

aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
parameters = cv2.aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

i = 0
while True:
    ret, img = cap.read()
    # print(img.shape)
    cv2.imshow('Webcam', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
   # img = cv2.aruco.drawDetectedMarkers(img, markerCorners, markerIds)
    c = cv2.waitKey(1)
    if c == 27:
        break
    if c == ord('q'):
        cv2.imwrite("image_rotation" + str(i) + ".jpg", img)
        i += 1

cap.release()
cv2.destroyAllWindows()