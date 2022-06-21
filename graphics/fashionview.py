#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt & other imports

from pickle import FALSE
from random import randint
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
import pyvista as pv
from pyvistaqt import QtInteractor

# Setting the Qt bindings for QtPy
import os
os.environ["QT_API"] = "pyqt6"

from path import texture_path

class PyVistaView (qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setObjectName("PyVistaView")
		
		# create the frame
		self.frame = qtw.QFrame()
	
        # add the pyvista interactor object
		self.plotter = QtInteractor(self.frame)
		self.plotter.set_background('black')

		camera = pv.Camera()
		self.plotter.camera.position = (1.1, 1.5, 0)
		self.plotter.camera.zoom(1.5)
		self.plotter.add_axes()
		self.plotter.camera = camera
		
		self.shirt = pv.read("graphics/shirt.obj")

		#example texture
		# self.texture = pv.read_texture('/Users/rkoop/Documents/cdvbw22/githubrepo/textures/3.png')
		# self.plotter.add_mesh(self.shirt, show_edges=False, texture=self.texture)
		self.set_texture('/Users/rkoop/Documents/cdvbw22/githubrepo/textures/3.png')
	
		self.plotter.reset_camera()
	

	def set_texture(self, str_img):
		#self.str_img = '/Users/rkoop/Documents/cdvbw22/githubrepo/textures/3.png'
		self.texture = pv.read_texture(str_img)
		self.plotter.add_mesh(self.shirt, show_edges=False, texture = self.texture)

	
	@qtc.pyqtSlot(str)
	def get_img(self, str_img):
		print('recieved img path name', str_img)

		self.img_value = randint(0,18)
		self.text_path = (texture_path + str_img + self.img_value)
		
		self.plotter.add_mesh

