#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt & other imports

from PyQt6 import QtWidgets as qtw
import pyvista as pv
from pyvistaqt import QtInteractor

# Setting the Qt bindings for QtPy
import os
os.environ["QT_API"] = "pyqt6"


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
		self.texture = pv.read_texture('/Users/rkoop/Documents/cdvbw22/githubrepo/textures/3.png')

		shirt = pv.read("graphics/shirt.obj")
		

		self.plotter.add_mesh(shirt, show_edges=False, texture=self.texture)

		#self.plotter(texture = self.texture)
	
		self.plotter.reset_camera()