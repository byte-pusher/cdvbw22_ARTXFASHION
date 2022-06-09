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
from gui.img_widget import ImgWidgetBig
from gui.pic_utils import img_creator


img_path = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'

class	SideChoiceWin(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#get list of filenames
		self.list_img_files = img_creator.get_file_list(img_path)

		#create list of numbers
		self.nb_list = []
		self.nb_list = img_creator.get_indices(9, self.nb_list)

		#create btn
		self.btn_all = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_FileDialogListView),
										 '&', self)

		#create mirror area
		self.mirror = qtw.QLabel()
		self.mirror.setStyleSheet("background : lightblue")

		#create img area
		self.set_img_widget()

		#st img on label with stacked laqout
		#self.stack = qtw.QLabel()
		#self.stack_layout = qtw.QStackedLayout()
		##self.stack_layout.addWidget(self.img_choice_big)
		#self.stack.setLayout(self.stack_layout)
		#create views
		#self.set_stacked_views()

		#create img big area
		#self.focus_img = qtw.QLabel()

		#Create overall layout and assemble
		self.overall_layout = qtw.QGridLayout()
		self.overall_layout.addWidget(self.mirror, 0, 0, 6, 4)
		self.overall_layout.addWidget(self.img_choice_big, 3, 5, 3, 1)
		#self.overall_layout.addWidget(self.stack, 0, 5, 6, 1)
		self.setLayout(self.overall_layout)
		
	def set_img_widget(self):
		counter = 0
		i = 1
		j = 1
		self.btn = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_BrowserReload),
										 '&', self)
		self.btn.setGeometry(10, 10, 60, 40)
		self.btn.setStyleSheet("text-align : center; border-radius : 5; border : 1px solid white")
		self.img_choice_big = qtw.QWidget()
		self.img_choice_big_layout = qtw.QGridLayout()
		while (counter < 9):
			self.img = img_creator.get_img(img_path + self.list_img_files[self.nb_list[-counter]], 120)
			self.img_choice_big_layout.addWidget(self.img, i, j)
			i = i + 1
			counter = counter + 1
			if i == 4 or i == 7:
				j = j + 1
				i = 1
		#self.btn.clicked.connect(self.turn)
		self.img_choice_big_layout.addWidget(self.btn, 1, 0, 3, 1)
		self.img_choice_big.setLayout(self.img_choice_big_layout)

	def set_stacked_views(self):
		nb = 237 / 9
		i = 0
		while (i < 3):
			self.extend_list()
			self.set_img_widget()
			self.stack_layout.addWidget(self.img_choice_big)

	def extend_list(self):
		i = 0
		while (i < 9):
			x = randint(0, 236)
			if x not in self.nb_list:
				self.nb_list.append(x)
				i = i + 1

	#def turn(self):
		#self.img_choice_big


		
		

	