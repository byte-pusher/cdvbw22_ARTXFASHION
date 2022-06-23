#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt & other imports

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6.QtCore import pyqtSlot
from numpy import diff
import pyvista as pv
from pyvistaqt import QtInteractor

# Setting the Qt bindings for QtPy
import os
os.environ["QT_API"] = "pyqt6"
from path import texture_path, shirt_path
import random
import numpy as np


class PyVistaView (qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setObjectName("PyVistaView")
		
		# create the frame
		self.frame = qtw.QFrame()
		self.frame_i = 0
        # add the pyvista interactor object
		self.plotter = QtInteractor(self.frame)
		self.plotter.set_background('black')
	
		self.shirt = pv.read(shirt_path)
		
		self.last_angle = 0
		self.actor = self.plotter.add_mesh(self.shirt, show_edges=False)
		self.plotter.camera  = pv.Camera()
		print(self.plotter.camera.position)
		self.plotter.reset_camera()
		# self.plotter.camera.zoom(0.8)
		

	@pyqtSlot()
	def frames(self):
		pass

		focal = self.plotter.camera.focal_point
		# print(focal)
		# self.plotter.camera.focal_point = (focal[0],focal[1]+ 0.001, focal[2])
		# # self.plotter.update()



	@pyqtSlot(tuple)
	def updating(self, angles):
		azimuth = angles[1]
		if abs(azimuth - self.last_angle) < 10:
			self.plotter.camera.azimuth = azimuth
			self.last_angle = azimuth
		elif abs(azimuth - self.last_angle) < 15:
			azimuth = self.last_angle + (azimuth - self.last_angle)/1.5
			self.last_angle = azimuth
			self.plotter.camera.azimuth = azimuth
		elif abs(azimuth - self.last_angle) < 20:
			azimuth = self.last_angle + (azimuth - self.last_angle)/2
			self.last_angle = azimuth
			self.plotter.camera.azimuth = azimuth
		elif abs(azimuth - self.last_angle) < 25:
			azimuth = self.last_angle + (azimuth - self.last_angle)/2.5
			self.last_angle = azimuth
			self.plotter.camera.azimuth = azimuth
		elif abs(azimuth - self.last_angle) < 30:
			azimuth = self.last_angle + (azimuth - self.last_angle)/3
			self.last_angle = azimuth
			self.plotter.camera.azimuth = azimuth
		else:
			print("Before: " + str(self.last_angle))
			azimuth = self.last_angle + (azimuth - self.last_angle)/5
			self.last_angle = azimuth
			self.plotter.camera.azimuth = azimuth
			print("After: " + str(azimuth))
		# print(angles)
	
	@qtc.pyqtSlot(str)
	def get_img(self, str_img):
		self.texture = pv.read_texture(texture_path + str_img)
		self.plotter.remove_actor(self.actor)
		self.actor = self.plotter.add_mesh(self.shirt, show_edges=False, texture=self.texture)

	def hide(self):
		self.plotter.remove_actor(self.actor)

	@qtc.pyqtSlot()
	def show(self):
		self.plotter.add_mesh(self.shirt, show_edges=False, texture=self.texture)
		
	
	def image_array(self,): 
		path = texture_path
        # create array of image file paths
		files = os.listdir(path)
		images = []
		for file in files:
			if file.endswith(('.jpg', '.png', 'jpeg')):
				img_path = path + file
				images.append(img_path)
		return images

	@pyqtSlot(int)
	def scale(self, x_diff):
		
		# # (0.0, 1.7, 0.0) -> unterer Rand
		# # (0.0, 0.66, 0.0) -> oberer Rand
		self.plotter.camera.view_angle = 40.0

		
		
	@pyqtSlot(np.ndarray)
	def move(self, corners):
		# Links - rechts
		# rechts = 250
		# links = 380
		# focal_size = 0.4
		# pixel = 130
		# unit = focal_size / pixel
		# middle = 315
		# focal = self.plotter.camera.focal_point
		# avg_links_corners = (corners[0][0] + corners[3][0]) / 2
		# avg_rechts_corners = (corners[1][0] + corners[2][0]) / 2
		# marker_middle_x = (avg_links_corners + avg_rechts_corners) / 2
		# if marker_middle_x > middle:
		# 	calc_focal = (middle - avg_rechts_corners) * unit
		# else:
		# 	calc_focal = (middle - avg_links_corners) * unit

		# # Oben - unten
		# unten = 475
		# oben = 80
		# pixel = unten - oben
		# focal_size2 = 1.74 + 0.94
		# middle2 = (unten + oben) / 2
		# unit2 = (focal_size2 / pixel)
		# avg_oben_corners = (corners[0][1] + corners[1][1]) / 2
		# avg_unten_corners = (corners[2][1] + corners[3][1]) / 2
		# marker_middle_y = (avg_oben_corners + avg_unten_corners) / 2

		# if marker_middle_y > middle:
		# 	calc_focal_y = (middle2 - avg_unten_corners) * unit2
		# else:
		# 	calc_focal_y = (middle2 - avg_oben_corners) * unit2
		# print("y1: " + str(corners[2][1]) + " y2: ",  end='')
		# print(corners[3][1])


		# print(focal)
		# # self.plotter.camera.focal_point = (focal[0],focal[1] - 0.001, focal[2])
		# # print(focal)
		# # print(focal)
		# # # print(focal_x)
		# self.plotter.camera.focal_point = (calc_focal * -1.4, 1.6 + calc_focal_y * -1, focal[2])

		pass