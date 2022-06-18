#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt & other imports
from random import randint
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import sip

#own imports
from graphics.modelview import GlWidget
from gui.pic_utils import img_creator
from path import img_path

#set path to imported path
img_path = img_path

class	ChoiceWin(qtw.QWidget):
	#signal for finalwin
	emit_choice = qtc.pyqtSignal(str)

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
		self.btn_side = qtw.QPushButton('&', self)
		self.btn_side.setObjectName("btn_arrow_left")
		self.btn_side.setIcon(qtg.QIcon('gui/icons/arrow_left'))
		self.icon_size_side = qtc.QSize(60,60)
		self.btn_side.setMinimumSize(80,80)
		self.btn_side.setIconSize(self.icon_size_side)
										 
		
		#create btn area
		self.btn_block_side = qtw.QWidget()
		self.btn_block_side.setObjectName("btn_area_side")
		self.btn_block_side.layout = qtw.QVBoxLayout()
		self.btn_block_side.layout.addWidget(self.btn_side)
		self.btn_block_side.layout.addStretch()
		self.btn_block_side.setLayout(self.btn_block_side.layout)

		#create modelview
		self.modelview = GlWidget()

		#Create overall layout and assemble
		self.overall_layout = qtw.QGridLayout()
		self.overall_layout.addWidget(self.modelview, 0, 0, 15, 9)
		self.overall_layout.addWidget(self.img_choice, 13, 0, 3, 9)
		self.overall_layout.addWidget(self.btn_block_side, 0, 9, 15, 1)

		self.setLayout(self.overall_layout)
		#self.create_stack()
		
	# create widget for img choice
	def set_img_widget(self):
		self.btn_shuffle = qtw.QPushButton('&', self)
		self.btn_shuffle.setIcon(qtg.QIcon('gui/icons/shuffle'))
		self.btn_shuffle.setObjectName("btn_shuffle_bottom")
		self.icon_size_shuffle = qtc.QSize(60,60)
		self.btn_shuffle.setIconSize(self.icon_size_shuffle)
		self.img_choice = qtw.QWidget()
		self.img_choice_layout = qtw.QGridLayout()
	
		#img widgets per img and connected to their specific emit for finalview
		self.img0 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-1]], 160)
		self.img_choice_layout.addWidget(self.img0, 1, 0)
		self.img0.mousePressEvent = self.emit0
		self.img1 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-2]], 160)
		self.img_choice_layout.addWidget(self.img1, 1, 1)
		self.img1.mousePressEvent = self.emit1
		self.img2 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-3]], 160)
		self.img_choice_layout.addWidget(self.img2, 1, 2)
		self.img2.mousePressEvent = self.emit2

		# connect shuffle btn to ft (move connection to mainapp?)
		self.btn_shuffle.clicked.connect(self.shuffle)
		self.img_choice_layout.addWidget(self.btn_shuffle, 0, 1, 1, 1)
		self.img_choice.setLayout(self.img_choice_layout)

	#create emits for widgetchanges/viewchanges
	def emit0(self, event):
		self.emit_choice.emit(self.img0.name)
	def emit1(self, event):
		self.emit_choice.emit(self.img1.name)
	def emit2(self, event):
		self.emit_choice.emit(self.img2.name)
		
	#get 3 new random images in choice
	def shuffle(self):
		#hide & clear widget for img choice
		self.img_choice.hide()
		self.clear()
		#check len of list, reset if necessary
		if len(self.nb_list) > 230:
				self.nb_list = []
		#append three new numbers to list
		i = 0
		while i < 3:
			x = randint(0, 235)
			if x not in self.nb_list:
				self.nb_list.append(x)
				i = i + 1
		print("List of random img indices: ", self.nb_list)
		#set new imgs, ft always uses last three
		self.set_img_widget()
		self.overall_layout.addWidget(self.img_choice, 13, 0, 3, 9)
		self.setLayout(self.overall_layout)
		self.show()

	#clear widget
	def clear(self):
		self.overall_layout.removeWidget(self.img_choice)
		sip.delete(self.img_choice)
		self.img_choice = None

	



	



			



