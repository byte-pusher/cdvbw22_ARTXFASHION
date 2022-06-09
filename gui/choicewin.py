#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     



from random import randint
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc
from PyQt6 import sip
from gui.img_widget import ImgWidget
from gui.pic_utils import img_creator

img_path = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'

class	ChoiceWin(qtw.QWidget):
	emit_choice = qtc.pyqtSignal(object)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#get list of filenames
		self.list_img_files = img_creator.get_file_list(img_path)

		#create list of numbers
		self.nb_list_small = []
		self.nb_list = img_creator.get_indices(3, self.nb_list_small)

		##create img choice widget
		self.set_img_widget()

		#create btn
		self.btn_all = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_MediaSkipBackward),
										 '&', self)
		self.btn_all.setGeometry(10, 10, 60, 40)								 
		self.btn_all.setStyleSheet("text-align : center; border-radius : 5; border : 1px solid white")
		#create mirror area
		self.mirror = qtw.QLabel()
		self.mirror.setStyleSheet("background : lightblue")

		#create btn area
		self.btn_block = qtw.QWidget()
		self.btn_block.setStyleSheet("background : lightblue")
		self.btn_block.layout = qtw.QVBoxLayout()
		self.btn_block.layout.addWidget(self.btn_all)
		#self.btn_block.layout.addStretch()
		self.btn_block.setLayout(self.btn_block.layout)

		#Create overall layout and assemble
		self.overall_layout = qtw.QGridLayout()
		self.overall_layout.addWidget(self.mirror, 0, 0, 4, 4)
		self.overall_layout.addWidget(self.img_choice, 4, 0, 1, 5)
		self.overall_layout.addWidget(self.btn_block, 0, 4, 4, 1)
		self.setLayout(self.overall_layout)
		
		
	def set_img_widget(self):
		self.btn_right = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_BrowserReload),
										 '&', self)
		self.btn_right.setStyleSheet("text-align : center; border-radius : 5; border : 1px solid white")
		i = 1
		self.img_choice = qtw.QWidget()
		self.img_choice_layout = qtw.QHBoxLayout()
		# while (i < 4):
		# 	self.img = img_creator.get_img(img_path + self.list_img_files[self.nb_list[-i]], 160)
		# 	self.img_choice_layout.addWidget(self.img)
		# 	self.img.mousePressEvent = self.emit
		# 	i = i+1

		#MANUAL CREATION OF 3 IMG WIDGETS FOR  EASY CONNECTION
		self.img0 = img_creator.get_img(img_path + self.list_img_files[self.nb_list[-1]], 160)
		self.img_choice_layout.addWidget(self.img0)
		self.img0.mousePressEvent = self.emit0
		self.img1 = img_creator.get_img(img_path + self.list_img_files[self.nb_list[-2]], 160)
		self.img_choice_layout.addWidget(self.img1)
		self.img1.mousePressEvent = self.emit1
		self.img2 = img_creator.get_img(img_path + self.list_img_files[self.nb_list[-3]], 160)
		self.img_choice_layout.addWidget(self.img2)
		self.img2.mousePressEvent = self.emit2
		
		print(len(self.list_img_files))
		print(len(self.nb_list))
		self.btn_right.clicked.connect(self.shuffle)
		self.img_choice_layout.addWidget(self.btn_right)
		self.img_choice.setLayout(self.img_choice_layout)

	def emit0(self, event):
		self.emit_choice.emit(self.img0)
	
	def emit1(self, event):
		self.emit_choice.emit(self.img1)
	
	def emit2(self, event):
		self.emit_choice.emit(self.img2)
		

	def shuffle(self):
		self.img_choice.hide()
		self.clear()
		print(self.nb_list)
		i = 0
		while i < 3:
			x = randint(0, 236)
			if len(self.nb_list) > (len(self.list_img_files) - 3):
				self.nb_list = []
			if x not in self.nb_list:
				self.nb_list.append(x)
				i = i + 1
		print(self.nb_list)
		self.set_img_widget()
		self.overall_layout.addWidget(self.img_choice, 4, 0, 1, 5)
		self.setLayout(self.overall_layout)
		self.show()

	def clear(self):
		self.overall_layout.removeWidget(self.img_choice)
		sip.delete(self.img_choice)
		self.img_choice = None

			



