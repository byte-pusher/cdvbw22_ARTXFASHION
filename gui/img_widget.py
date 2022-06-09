 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/       

import os

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

from gui.pic_utils import img_creator
from gui.stylesheet import stylesheet

class ImgWidget(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.dirpath = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'
		self.files = [f for f in os.listdir(self.dirpath) if os.path.isfile(os.path.join(self.dirpath, f))]
		self.list = []

		self.btn_right = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_ArrowRight),
										 '&', self)

	#create img widget for choice of 3
	def create_img_widget(self, list):
		i = 1
		self.img_choice = qtw.QWidget()
		self.img_choice.layout = qtw.QHBoxLayout()
		while (i < 4):
			self.img = img_creator.get_img(self.dirpath + self.files[list[-i]], 160)
			self.img_choice.layout.addWidget(self.img)
			i = i+1
		self.img_choice.layout.addWidget(self.btn_right)
		self.img_choice.setLayout(self.img_choice.layout)
		return(self.img_choice)


class ImgWidgetBig(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.dirpath = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'
		self.files = [f for f in os.listdir(self.dirpath) if os.path.isfile(os.path.join(self.dirpath, f))]
		self.list = []

		self.btn_right = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_ArrowRight),
										 '&', self)
	#create img widget for side choice
	def create_img_widget(self,list):
		counter = 0
		i = 1
		j = 1
		self.btn = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_ArrowRight),
										 '&', self)
		self.btn.setStyleSheet(stylesheet)
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
		self.img_choice_big.layout.addWidget(self.btn, 1, 4, 5, 1)
		self.img_choice_big.setLayout(self.img_choice_big.layout)
		return(self.img_choice_big)

	#slot to recieve path
	@qtc.pyqtSlot(str)
	def set_path(self, dirpath):
		self.dirpath = dirpath

