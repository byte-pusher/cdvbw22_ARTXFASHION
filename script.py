import cv2
import mediapipe as mp
import time
from PoseModule import PoseDetector


cap = cv2.VideoCapture(0)
pTime = 0
detector = PoseDetector()
while True:
	success, img = cap.read()
	img = detector.findPose(img)
	lmList = detector.getPosition(img)
	print(lmList)

	cTime = time.time()
	fps = 1 / (cTime - pTime)
	pTime = cTime
	cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
	cv2.imshow("Image", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	cv2.waitKey(-1)
	break