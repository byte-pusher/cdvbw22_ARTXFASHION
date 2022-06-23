#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt & other imports

from email.mime import image
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
		self.plotter.camera.view_angle = 30.0

		
		
	@pyqtSlot(tuple)
	def move(self, mid_point):
		pass
		# pixel_width = 680
		# mid = 340

		# width = 2
		# fract = width / pixel_width
		# calc_mid = (mid_point[0] - mid) * fract
		# focal = self.plotter.camera.focal_point
		# print(focal)
		# # print(focal_x)
		# self.plotter.camera.focal_point = (calc_mid,focal[1], focal[2])