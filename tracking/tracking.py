import numpy as np
import cv2
from cv2 import aruco
import sys, time, math
from calibrating import *
import os
import matrix_to_euler
import time

# def image_array():

#     path = "/Users/mawinter/Desktop/rays/tracking/cal_imgs/"

#     # create array of image file paths
#     files = os.listdir(path)
#     images = []
#     for file in files:
#         if file.endswith(('.jpg', '.png', 'jpeg')):
#             img_path = path + file
#             images.append(img_path)
#     return images

# images = image_array()

# # create board
# board = aruco.CharucoBoard_create(
#         squaresX=6, 
#         squaresY=8, 
#         squareLength=0.04, 
#         markerLength=0.02, 
#         dictionary=aruco.Dictionary_get(aruco.DICT_5X5_50))

# # calibrate camera
# allCorners,allIds,imsize=read_chessboards(images, board)
# ret, camera_matrix, camera_distortion, rvecs, tvecs = calibrate_camera(allCorners,allIds,imsize,board)
# markerLength=0.05,

# #... 180 deg rotation matrix around the x axis
# R_flip = np.zeros((3,3), dtype=np. float32)
# R_flip[0,0] = 1.0
# R_flip [1,1] =-1.0
# R_flip[2,2] =-1.0

# #--- Define the aruco dictionary
# aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
# parameters = aruco.DetectorParameters_create()

# #- - - Capture the videocamera
# cap = cv2.VideoCapture(0)

# while True:
#     #-- Convert in gray scale
#     time.sleep(2)
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     #-- Find all the aruco markers in the image
#     corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, parameters=parameters)

#     if ids != None:
#         # detect single marker
#         rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, markerLength[0], camera_matrix, camera_distortion)
       
#         #-- Draw the detected marker and put a reference frame over it
#         aruco.drawDetectedMarkers(frame, corners)
        
#         # convert axis angle representation into rotation matrix
#         R_ct = np.matrix(cv2.Rodrigues(rvec)[0])
#         R_tc = R_ct.T 

#         # convert rotation matrix to euler angles
#         roll_marker, pitch_marker, yaw_marker = matrix_to_euler.rotationMatrixToEulerAngles(R_flip*R_tc) 
