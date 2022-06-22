#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt & other imports

from email.mime import image
from PyQt6 import QtWidgets as qtw
from PyQt6.QtCore import pyqtSlot
from numpy import diff
import pyvista as pv
from pyvistaqt import QtInteractor

# Setting the Qt bindings for QtPy
import os
os.environ["QT_API"] = "pyqt6"
from path import texture_path
import random



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
	
		self.shirt = pv.read("graphics/shirt.obj")
	
		
		self.actor = self.plotter.add_mesh(self.shirt, show_edges=False)
		self.plotter.camera  = pv.Camera()
		print(self.plotter.camera.position)
		self.plotter.reset_camera()
		# self.plotter.camera.zoom(0.8)
	
	@pyqtSlot(tuple)
	def updating(self, angles):
		azimuth = angles[1]

		self.plotter.camera.azimuth = azimuth
		print(angles)
	
	@pyqtSlot(str)
	def get_img(self, str_img):
		self.texture = pv.read_texture(texture_path + str_img)
		self.plotter.remove_actor(self.actor)
		self.actor = self.plotter.add_mesh(self.shirt, show_edges=False, texture=self.texture)

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
		self.frame_i += 1

		if self.frame_i % 20 == 0:
			# pos1, pos2, pos3 = self.plotter.camera.position
			# self.plotter.camera.position = (pos1 , pos2, pos3 + 0.05)
			# self.plotter.camera.render()
			print(self.plotter.camera.view_angle)
			self.plotter.camera.focal_point = (0.0,2.0,0.0)
			self.plotter.camera.view_angle = 60.0
			print("asd")
		# if self.frame_i % 30 == 0:
			# self.plotter.camera.view_angle = 30.0

		# 	self.plotter.camera.zoom(0.2)
		# 	self.plotter.reset_camera()
			# print("zwei")
		# self.plotter.update()
		# print(self.frame_i)
		# print(x_diff)