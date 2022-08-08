import cv2
from cv2 import aruco
import time

aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
parameters = cv2.aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)

# Take Calibrating Pictures Of Charuco Board to calibrate the Camera
# ~10 clear Picture should suffice
# Take them from multiple angles
i = 0
while True:
    ret, img = cap.read()
    cv2.imshow('Webcam', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    c = cv2.waitKey(1)
    if c == 27:
        break
    if c == ord('q'):
        cv2.imwrite("image_rotation" + str(i) + ".jpg", img)
        i += 1

cap.release()
cv2.destroyAllWindows()