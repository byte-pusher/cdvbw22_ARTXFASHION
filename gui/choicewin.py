#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     



from ast import While
from random import randint
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc
from PyQt6 import sip

#own imports
from graphics.modelview import GlWidget
from gui.pic_utils import img_creator

#path import from path.py
from path import img_path
img_path = img_path

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
		self.btn_side = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_MediaSkipBackward),
										 '&', self)
		self.btn_side.setGeometry(10, 10, 60, 40)								 
		self.btn_side.setStyleSheet("text-align : center; border-radius : 5; border : 1px solid white")

		self.btn_wear = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogApplyButton),
										 '&', self)
		self.btn_wear.setGeometry(10, 10, 60, 40)								 
		self.btn_wear.setStyleSheet("text-align : center; border-radius : 5; border : 1px solid white")

		#create btn area
		self.btn_block_side = qtw.QWidget()
		self.btn_block_side.setStyleSheet("background : black")
		self.btn_block_side.layout = qtw.QVBoxLayout()
		self.btn_block_side.layout.addStretch()
		self.btn_block_side.layout.addWidget(self.btn_wear)
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
		self.btn_shuffle = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_BrowserReload),
										 '&', self)
		self.btn_shuffle.setStyleSheet("text-align : center; border-radius : 5; border : 1px solid white")
		i = 1
		self.img_choice = qtw.QWidget()
		self.img_choice_layout = qtw.QGridLayout()
		# while (i < 4):
		# 	self.img = img_creator.get_img(img_path + self.list_img_files[self.nb_list[-i]], 160)
		# 	self.img_choice_layout.addWidget(self.img)
		# 	self.img.mousePressEvent = self.emit
		# 	i = i+1

		#MANUAL CREATION OF 3 IMG WIDGETS FOR  EASY CONNECTION
		self.img0 = img_creator.get_img(img_path + self.list_img_files[self.nb_list[-1]], 160)
		self.img_choice_layout.addWidget(self.img0, 1, 0)
		self.img0.mousePressEvent = self.emit0
		self.img1 = img_creator.get_img(img_path + self.list_img_files[self.nb_list[-2]], 160)
		self.img_choice_layout.addWidget(self.img1, 1, 1)
		self.img1.mousePressEvent = self.emit1
		self.img2 = img_creator.get_img(img_path + self.list_img_files[self.nb_list[-3]], 160)
		self.img_choice_layout.addWidget(self.img2, 1, 2)
		self.img2.mousePressEvent = self.emit2
		
		print("Number of paintings: " , len( self.list_img_files))
		self.btn_shuffle.clicked.connect(self.shuffle)
		self.img_choice_layout.addWidget(self.btn_shuffle, 0, 1, 1, 1)
		self.img_choice.setLayout(self.img_choice_layout)

	#create emits for widgetchanges/viewchanges
	def emit0(self, event):
		self.emit_choice.emit(self.img0)
	
	def emit1(self, event):
		self.emit_choice.emit(self.img1)
	
	def emit2(self, event):
		self.emit_choice.emit(self.img2)
		
	#get 3 new random images
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

	#clear widget
	def clear(self):
		self.overall_layout.removeWidget(self.img_choice)
		sip.delete(self.img_choice)
		self.img_choice = None


	# create stack of img widgets
	def create_stack(self):
		self.stack = qtw.QStackedWidget()
		self.index_list = []
		self.index_list = img_creator.get_indices(229, self.index_list)
		print(self.index_list)
		self.img_widgets = {}
		#for i in range(len(self.list_img_files)):
		i = 0
		while i < 235:
			name = self.list_img_files[i]
			self.img_widgets[name + '_label'] = img_creator.get_img(img_path + self.list_img_files[i], 120 )
			self.stack.addWidget(self.img_widgets[name + '_label'])
			i = i + 1
			print(name)
		self.overall_layout.addWidget(self.stack, 4, 0, 1, 5)
		self.stack.setCurrentIndex(1)
		print("stack sucessfull added")
		self.setLayout(self.overall_layout)
		#self.show()




	
	# #trigger animations for modelview
	# def keyPressEvent(self, event):
	# 	if event.key() == qtc.Qt.Key.Key_Up:
	# 		self.modelview.spin_up()
	# 	if event.key() == qtc.Qt.Key.Key_Down:
	# 		self.modelview.spin_down()
	# 	if event.key() == qtc.Qt.Key.Key_Left:
	# 		self.modelview.spin_left()
	# 	if event.key() == qtc.Qt.Key.Key_Right:
	# 		self.modelview.spin_right()
	# 	if event.key() == qtc.Qt.Key.Key_Space:
	# 		self.modelview.spin_none()

			



