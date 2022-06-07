 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/       

import os
import sys
from random import seed
from random import randint
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

class img_creator(qtw.QWidget):
	
	# emit_img = qtc.pyqtSignal(object)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		
		dirpath = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'
		self.filelist = self.get_file_list(dirpath)
		self.create_all_img(self.dirpath)

	def get_img(filepath, scale):
		img = qtw.QLabel()
		pixmap = qtg.QPixmap(filepath)
		img.setPixmap(pixmap.scaled(scale, scale, qtc.Qt.AspectRatioMode.KeepAspectRatio))
		img.setAlignment((qtc.Qt.AlignmentFlag.AlignCenter))
		#img.setStyleSheet("background : darkgrey")
		return(img)
		#self.emit_img(self.img)

	# def emit_img(self, img_obj):
	# 	self.emit_img(img_obj)

	def get_file_list(dirpath):
		path = dirpath
		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
		return(files)

	def random_choice(seed_int):
		seed(seed_int)
		v01 = randint(0, 236)
		v02 = randint(0, 236)
		v03 = randint(0, 236)
		return(v01, v02, v03)

	#
	def get_indices(nb, list):
		count = 0
		x = 0
		while(count < nb):
			x = randint(0, 236)
			if x not in list:
				list.append(x)
				count = count + 1
			if len(list) > 230:
				list = []
		return(list)



	



	



