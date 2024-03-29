from distutils.log import error
from tkinter import image_names
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import cv2
import mediapipe as mp
import numpy as np
from cv2 import aruco
import time
import os
from tracking.calibrator import Calibrator
import math

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose(enable_segmentation=True)

class Worker(QObject):
    angles = pyqtSignal(tuple)
    x_diff = pyqtSignal(int)
    y_height = pyqtSignal(int)
    x_diff_always = pyqtSignal(tuple)
    frames = pyqtSignal()
    move = pyqtSignal(tuple)
    # method which will execute algorithm in another thread
    def run(self):
        print("Starting Thread.")
        cal = Calibrator()

        allCorners, allIds, imsize = cal.read_chessboards(cal.images, cal.board)
        ret, camera_matrix, camera_distortion, rvecs, tvecs = cal.calibrate_camera(allCorners,allIds,imsize,cal.board)
     
        markerLength=5

        #... 180 deg rotation matrix around the x axis
        R_flip = np.zeros((3,3), dtype=np. float32)
        R_flip[0,0] = 1.0
        R_flip [1,1] =-1.0
        R_flip[2,2] =-1.0

        #--- Define the aruco dictionary
        parameters = aruco.DetectorParameters_create()

        # capture from web cam
        cap = cv2.VideoCapture(0)
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        while True:
            self.frames.emit()
            #-- Convert in gray scale
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.emit_angles(frame, gray, parameters, cal, markerLength, camera_matrix, camera_distortion, R_flip)
            self.x_diff_always_func(frame)


            c = cv2.waitKey(1)
            if c == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    

    def x_diff_always_func(self, frame):
        results = pose.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        try:
            r_x = int(frame.shape[1] * results.pose_landmarks.landmark[11].x)
            l_x = int(frame.shape[1] * results.pose_landmarks.landmark[12].x)
            r_y = int(frame.shape[1] * results.pose_landmarks.landmark[11].y)
            l_y = int(frame.shape[1] * results.pose_landmarks.landmark[12].y)
            x_difference = r_x - l_x
            height = (r_y + l_y) / 2
            self.x_diff_always.emit((x_difference, height))
        except Exception as e:
            pass


    def x_difference(self, frame):
        results = pose.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        try:
            r_x = int(frame.shape[1] * results.pose_landmarks.landmark[11].x)
            l_x = int(frame.shape[1] * results.pose_landmarks.landmark[12].x)
            r_y = int(frame.shape[1] * results.pose_landmarks.landmark[11].y)
            l_y = int(frame.shape[1] * results.pose_landmarks.landmark[12].y)
            x_difference = r_x - l_x
            height = (r_y + l_y) / 2
            self.x_diff.emit(x_difference)
        except Exception as e:
            pass

    def emit_angles(self, frame, gray, parameters, cal, markerLength, camera_matrix, camera_distortion, R_flip):
        #-- Find all the aruco markers in the image
            corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=cal.aruco_dict, parameters=parameters)
            if ids is not None:
                # corners2 = corners[0][0]
                # self.mid_point.emit(corners2)
                # print(corners[0])
                aruco.drawDetectedMarkers(frame, corners)
                # detect single marker
                rvec_all, tvec_all, _ = aruco.estimatePoseSingleMarkers(corners, markerLength, camera_matrix, camera_distortion)
                #-- Draw the detected marker and put a reference frame over it
                rvec = rvec_all[0][0]
                tvec = tvec_all[0][0]
                rvec_flipped = rvec * -1
                tvec_flipped = tvec * -1
                self.move.emit((tvec_all[0][0][2],))
                rotation_matrix, jacobian = cv2.Rodrigues(rvec_flipped)
                realworld_tvec = np.dot(rotation_matrix, tvec_flipped)
                pitch, roll, yaw = self.rotationMatrixToEulerAngles(rotation_matrix)
                # convert axis angle representation into rotation matrix
                R_ct = np.matrix(cv2.Rodrigues(rvec)[0])
                R_tc = R_ct.T 
        
                # convert rotation matrix to euler angles
                roll_marker, pitch_marker, yaw_marker = self.rotationMatrixToEulerAngles(R_flip*R_tc)
              
                self.angles.emit((math.degrees(roll_marker),math.degrees(pitch_marker),math.degrees(pitch_marker)))
                if (abs(math.degrees(pitch_marker)) < 15):
                    self.x_difference(frame)
        
    def isRotationMatrix(self, R):
        Rt = np.transpose(R)
        shouldBeIdentity = np.dot(Rt, R)
        I = np.identity(3, dtype = R.dtype)
        n = np.linalg.norm(I - shouldBeIdentity)
        return n < 1e-6

    def rotationMatrixToEulerAngles(self, R) :
        assert(self.isRotationMatrix(R))
        sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
        singular = sy < 1e-6
        if  not singular :
            x = math.atan2(R[2,1] , R[2,2])
            y = math.atan2(-R[2,0], sy)
            z = math.atan2(R[1,0], R[0,0])
        else :
            x = math.atan2(-R[1,2], R[1,1])
            y = math.atan2(-R[2,0], sy)
            z = 0
        return np.array([x, y, z])

class Webcam(QWidget):
 
    def __init__(self, parent=None):
        super().__init__()
        # use button to invoke slot with another text and color
        
 
        # create thread
        self.thread = QThread()
        # create object which will be moved to another thread
        self.worker = Worker()
        # move object to another thread
        self.worker.moveToThread(self.thread)
        # connect started signal to run method of object in another thread
        self.thread.started.connect(self.worker.run)
        # start thread
        self.thread.start()
 

