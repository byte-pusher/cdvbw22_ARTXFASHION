import cv2
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose(enable_segmentation=True)

capture = cv2.VideoCapture(0)

while True:
	success, img = capture.read()
	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	results = pose.process(imgRGB)
	try:
		pr = int(img.shape[1] * results.pose_landmarks.landmark[11].x)
		pr2 = int(img.shape[0] * results.pose_landmarks.landmark[11].y)
		pl = int(img.shape[1] * results.pose_landmarks.landmark[12].x)
		pl2 = int(img.shape[0] * results.pose_landmarks.landmark[12].y)
		cv2.circle(img,(pl,pl2), radius=1, color=(255,0,255), thickness=6)
		cv2.circle(img,(pr,pr2), radius=1, color=(255,0,0), thickness=6)
		x_difference = pr - pl
		y_difference = pr2 - pl2
		cv2.putText(img, "x difference " + str(int(x_difference)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)
		# cv2.putText(img, "y difference" + str(int(y_difference)), (70, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)
	except:
		pass
	cv2.imshow("Image", img)
	c = cv2.waitKey(1)
	if c == 27:
		break
capture.release()
cv2.destroyAllWindows()
