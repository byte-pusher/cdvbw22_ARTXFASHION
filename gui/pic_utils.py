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
	emit_choice = qtc.pyqtSignal(object)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		dirpath = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'
		self.filelist = self.get_file_list(dirpath)

	def get_img(filepath, scale):
		img = qtw.QLabel()
		pixmap = qtg.QPixmap(filepath)
		img.setPixmap(pixmap.scaled(scale, scale, qtc.Qt.AspectRatioMode.KeepAspectRatio))
		img.setAlignment((qtc.Qt.AlignmentFlag.AlignCenter))
		return(img)

	
	# def get_img(filepath, scale):
	# 	img = qtw.QLabel()
	# 	pixmap = qtg.QPixmap(filepath)
	# 	img.setPixmap(pixmap.scaled(scale, scale, qtc.Qt.AspectRatioMode.KeepAspectRatio))
	# 	img.setAlignment((qtc.Qt.AlignmentFlag.AlignCenter))
	# 	return(img)

	def get_img(self, filepath, scale):
		self.img = qtw.QLabel()
		self.pixmap = qtg.QPixmap(filepath)
		self.img.setPixmap(self.pixmap.scaled(scale, scale, qtc.Qt.AspectRatioMode.KeepAspectRatio))
		self.img.setAlignment((qtc.Qt.AlignmentFlag.AlignCenter))
		self.img.mousePressEvent = self.emit_choice.emit(self.img)
		return(self.img)


	def get_file_list(dirpath):
		path = dirpath
		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
		return(files)

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



	



	



