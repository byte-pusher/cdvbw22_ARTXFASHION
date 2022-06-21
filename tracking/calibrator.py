import cv2
from cv2 import aruco
import numpy as np
import os
class Calibrator:
    def __init__(self, parent=None):
        super().__init__()
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
        self.board = aruco.CharucoBoard_create(
                    squaresX=6, 
                    squaresY=8, 
                    squareLength=0.04, 
                    markerLength=0.02, 
                    dictionary=aruco.Dictionary_get(aruco.DICT_5X5_50))
        self.images = self.image_array()

    def read_chessboards(images, board):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)

        print("POSE ESTIMATION STARTS:")
        allCorners = []
        allIds = []
        decimator = 0
        # SUB PIXEL CORNER DETECTION CRITERION
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.00001)

        for im in images:
            print("=> Processing image {0}".format(im))
            frame = cv2.imread(im)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict)

            if len(corners)>0:
                # SUB PIXEL DETECTION
                for corner in corners:
                    cv2.cornerSubPix(gray, corner,
                                     winSize = (3,3),
                                     zeroZone = (-1,-1),
                                     criteria = criteria)
                res2 = cv2.aruco.interpolateCornersCharuco(corners,ids,gray,board)
                if res2[1] is not None and res2[2] is not None and len(res2[1])>3 and decimator%1==0:
                    allCorners.append(res2[1])
                    allIds.append(res2[2])

            decimator+=1

        imsize = gray.shape
        return allCorners,allIds,imsize

    def calibrate_camera(allCorners,allIds,imsize, board):
        print("CAMERA CALIBRATION")

        cameraMatrixInit = np.array([[ 1000.,    0., imsize[0]/2.],
                                     [    0., 1000., imsize[1]/2.],
                                     [    0.,    0.,           1.]])

        distCoeffsInit = np.zeros((5,1))
        flags = (cv2.CALIB_USE_INTRINSIC_GUESS + cv2.CALIB_RATIONAL_MODEL + cv2.CALIB_FIX_ASPECT_RATIO)
        #flags = (cv2.CALIB_RATIONAL_MODEL)
        (ret, camera_matrix, distortion_coefficients0,
         rotation_vectors, translation_vectors,
         stdDeviationsIntrinsics, stdDeviationsExtrinsics,
         perViewErrors) = cv2.aruco.calibrateCameraCharucoExtended(
                          charucoCorners=allCorners,
                          charucoIds=allIds,
                          board=board,
                          imageSize=imsize,
                          cameraMatrix=cameraMatrixInit,
                          distCoeffs=distCoeffsInit,
                          flags=flags,
                          criteria=(cv2.TERM_CRITERIA_EPS & cv2.TERM_CRITERIA_COUNT, 10000, 1e-9))

        return ret, camera_matrix, distortion_coefficients0, rotation_vectors, translation_vectors

    def image_array(self,): 
        path = "/Users/mawinter/Desktop/rays/tracking/cal_imgs/"
        # create array of image file paths
        files = os.listdir(path)
        images = []
        for file in files:
            if file.endswith(('.jpg', '.png', 'jpeg')):
                img_path = path + file
                images.append(img_path)
        return images
