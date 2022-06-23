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
	
		self.max_oben = 0
		self.max_unten = 0
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

		# self.plotter.camera.azimuth = azimuth
		# print(angles)
	
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

	@pyqtSlot(int)
	def scale(self, x_diff):
		# # (0.0, 1.7, 0.0) -> unterer Rand
		# # (0.0, 0.66, 0.0) -> oberer Rand
		self.plotter.camera.view_angle = 30.0

		
		
	@pyqtSlot(np.ndarray)
	def move(self, corners):
		focal_size = 0.4
		pixel = 135
		unit = 0.4 / 135
		middle = 292.5
		focal = self.plotter.camera.focal_point
		print(focal)
		# print(focal)
		# # print(focal_x)
		self.plotter.camera.focal_point = (focal[0] + 0.001 ,focal[1], focal[2])