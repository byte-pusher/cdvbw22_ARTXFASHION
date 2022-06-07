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

from gui.pic_utils import img_creator


class ImgWidget(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.dirpath = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'
		self.files = [f for f in os.listdir(self.dirpath) if os.path.isfile(os.path.join(self.dirpath, f))]
		#print(self.files[3])
		self.list = []

	#not sucessfully connected yet
	def create_side(self,list):
		counter = 0
		i = 1
		j = 1
		self.img_choice_big = qtw.QWidget()
		self.img_choice_big.layout = qtw.QGridLayout()
		while (counter < 15):
			self.img = img_creator.get_img(self.dirpath + self.files[list[-counter]], 160)
			self.img_choice_big.layout.addWidget(self.img, i, j)
			i = i+1
			counter = counter + 1
			if i == 6 or i == 11:
				j = j + 1
				i = 1
		return(self.img_choice_big)







		#print(self.files)
		i = 0
		while (i < 237):
			widget = self.create(self.files[i],self.files[i])
			self.list.append(widget)
			i = i + 1
		print(*self.list[3])
			#pd.to_pickle(widget, self.files[i])

	def create(self, imagepath, name):
		name = qtw.QLabel()
		pixmap = qtg.QPixmap(self.dirpath + imagepath)
		#pixmap = 
		name.setPixmap(pixmap.scaled(320,320, qtc.Qt.AspectRatioMode.KeepAspectRatio))
		name.setAlignment((qtc.Qt.AlignmentFlag.AlignCenter))
		#self.name = name
		return(pixmap)

	@qtc.pyqtSlot(str)
	def set_path(self, dirpath):
		self.dirpath = dirpath

