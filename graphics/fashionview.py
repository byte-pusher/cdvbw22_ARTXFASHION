#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt & other imports

from PyQt6 import QtWidgets as qtw
from PyQt6.QtCore import pyqtSlot
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
		#example texture
		self.texture = pv.read_texture(texture_path)
		# axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
		# self.plotter.add_axes_at_origin(line_width=5)
		shirt = pv.read("graphics/shirt.obj")
		

	
		
		self.plotter.add_mesh(shirt, show_edges=False, texture=self.texture)
		self.plotter.camera  = pv.Camera()
		print(self.plotter.camera.position)
		self.plotter.reset_camera()	
	
	@pyqtSlot(tuple)
	def updating(self, angles):
		azimuth = angles[1]

		self.plotter.camera.azimuth = azimuth
		print(angles)