#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt & other imports

from cmath import inf
from pickle import TRUE
from typing import Tuple
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6.QtCore import pyqtSlot
from numpy import diff
import pyvista as pv
from pyvistaqt import QtInteractor
from random import randint

# Setting the Qt bindings for QtPy
import os
os.environ["QT_API"] = "pyqt6"

from path import texture_path, shirt_path, img_path
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
		
		self.active = 0
		print(self.plotter.camera.position)
		self.plotter.reset_camera()
		print("foc" + str(self.plotter.camera.focal_point))
		# self.plotter.camera.zoom(0.8)
		

	@qtc.pyqtSlot()
	def frames(self):
		pass

		focal = self.plotter.camera.focal_point
		# print(focal)
		# self.plotter.camera.focal_point = (focal[0],focal[1]+ 0.001, focal[2])
		# # self.plotter.update()



	@qtc.pyqtSlot(tuple)
	def updating(self, angles):
		# azimuth = angles[1]
		# if abs(azimuth - self.last_angle) < 10:
		# 	self.plotter.camera.azimuth = azimuth
		# 	self.last_angle = azimuth
		# elif abs(azimuth - self.last_angle) < 15:
		# 	azimuth = self.last_angle + (azimuth - self.last_angle)/2
		# 	self.last_angle = azimuth
		# 	self.plotter.camera.azimuth = azimuth
		# elif abs(azimuth - self.last_angle) < 20:
		# 	azimuth = self.last_angle + (azimuth - self.last_angle)/2.5
		# 	self.last_angle = azimuth
		# 	self.plotter.camera.azimuth = azimuth
		# elif abs(azimuth - self.last_angle) < 25:
		# 	azimuth = self.last_angle + (azimuth - self.last_angle)/3
		# 	self.last_angle = azimuth
		# 	self.plotter.camera.azimuth = azimuth
		# elif abs(azimuth - self.last_angle) < 30:
		# 	azimuth = self.last_angle + (azimuth - self.last_angle)/4
		# 	self.last_angle = azimuth
		# 	self.plotter.camera.azimuth = azimuth
		# else:
		# 	print("Before: " + str(self.last_angle))
		# 	azimuth = self.last_angle + (azimuth - self.last_angle)/8
		# 	self.last_angle = azimuth
		# 	self.plotter.camera.azimuth = azimuth
		# 	print("After: " + str(azimuth))
		# print(angles)
		pass
	
	@qtc.pyqtSlot(str)
	def get_img(self, str_img):
		self.plotter.remove_actor(self.actor)
		texture_dir = str_img[:-4]

		try:
			path = texture_path + texture_dir + '/'
			files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
		except:
			files = []

		if not files:
			self.texture = pv.read_texture(img_path + str_img)
			self.actor = self.plotter.add_mesh(self.shirt, show_edges=False, texture = self.texture)
			print("Error: no dirs with generated textures")
		else:
			texture_nb = len(files)
			rand = randint(0,texture_nb)
			self.texture = pv.read_texture(texture_path + texture_dir + '.png')
			self.actor = self.plotter.add_mesh(self.shirt, show_edges=False, texture=self.texture)
			print(texture_path + texture_dir + '/' + str(rand) + '.png')
		
	

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

	@qtc.pyqtSlot(int)
	def scale(self, x_diff):
		# print(x_diff)
		# # (0.0, 1.7, 0.0) -> unterer Rand
		# # (0.0, 0.66, 0.0) -> oberer Rand
		default = 40
		fixed = 170
		scale = 175 - x_diff
		i = 0.15
		self.plotter.camera.view_angle = default + scale * i
	

		# Marius 170

	@pyqtSlot(tuple)
	def move_up(self, up):
		pass


	@qtc.pyqtSlot()	
	def activate(self):
		if self.active is 1:
			self.active = 0
			self.plotter.camera.focal_point = (0.0, 1.2723920047283173, 0.02216850221157074)
		else:
			self.active = 1
		print(self.active)



	@pyqtSlot(tuple)
	def move(self, info):
		# print(info)
		# if 165 < xdiff and xdiff < 180:
		# 	shoulder_m = 380
		# 	shoulder_d = 420
		# d height 1.265
		print(self.active)
		# m height 1.18
		if self.active is 1:

			base = 420
			diff = info[1] - 420
			unit = 0.0028

			focal = self.plotter.camera.focal_point


			self.plotter.camera.focal_point = (focal[0], 1.265 + unit * diff, focal[2])

		# focal = self.plotter.camera.focal_point
		# mid_y = mids[1]
		# normal = 380
		# diff = 380 - mids[1]
		# i = 0.001
		# print(focal)
		# self.plotter.camera.focal_point = (focal[0], 1.28 + diff, focal[2])
		
		

	