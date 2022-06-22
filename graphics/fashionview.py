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
	
        # add the pyvista interactor object
		self.plotter = QtInteractor(self.frame)
		self.plotter.set_background('black')
	
		self.shirt = pv.read("graphics/shirt.obj")
		img_array = self.image_array()
		i = random.randint(0, len(img_array) - 1)
		self.texture = pv.read_texture(img_array[i])
	
		
		self.actor = self.plotter.add_mesh(self.shirt, show_edges=False, texture=self.texture)
		self.plotter.camera  = pv.Camera()
		print(self.plotter.camera.position)
		self.plotter.reset_camera()	
	
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