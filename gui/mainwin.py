 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     


from random import seed
from random import randint
from PyQt6 import sip

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc
from gui.img_widget import ImgWidget

from gui.pic_utils import img_creator

img_path = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'

class	MainWindow((qtw.QMainWindow)):
	"Main Window of Magic Mirror"
	 #sigs

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	

		#set basic window & geometry
		self.setWindowTitle("Magic Mirror")
		self.setGeometry(400, 700, 800, 100)

		#menu for acess of actions
		self.menubar = self.menuBar()
		self.menu = self.menubar.addMenu("Management")

		#set actions for easy program management
		self.restartAction = qtg.QAction(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_BrowserReload),
										'&Restart', self)
		self.exitAction = qtg.QAction(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogCancelButton),
										'&Terminate', self)

		#add actions to menubar
		self.menu.addAction(self.restartAction)
		self.menu.addAction(self.exitAction)

		#buttons
		self.btn_left = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_ArrowLeft),
										 '&', self)
		self.btn_right = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_ArrowRight),
										 '&', self)

		self.list_img_files = img_creator.get_file_list(img_path)
		#standartchoice: labels for images & set images on label via pixmap
		self.img01 = img_creator.get_img(img_path + self.list_img_files[randint(0, 236)], 320)
		self.img02 = img_creator.get_img(img_path + self.list_img_files[randint(0, 236)], 320)
		self.img03 = img_creator.get_img(img_path + self.list_img_files[randint(0, 236)], 320)

		# #widget for picture choice
		self.img_choice = qtw.QWidget()
		self.img_choice.layout = qtw.QHBoxLayout()
		self.img_choice.layout.addWidget(self.btn_left)
		self.img_choice.layout.addWidget(self.img01)
		self.img_choice.layout.addWidget(self.img02)
		self.img_choice.layout.addWidget(self.img03)
		self.img_choice.layout.addWidget(self.btn_right)
		self.img_choice.setLayout(self.img_choice.layout)

		#placeholder widget for output
		self.output = qtw.QLabel()
		self.output.setStyleSheet("background : darkgrey")


		# #generadte nbs small
		# self.nb_list_small = []
		# nbs = 0
		# x = 0
		# while(nbs < 3):
		# 	x = randint(0, 236)
		# 	if x not in self.nb_list_small:
		# 		self.nb_list_small.append(x)
		# 		nbs = nbs + 1
		# 	if len(self.nb_list_small > 230):
		# 		self.nb_list_small = []
		
		
		# #generate numbers big
		# self.nb_list_big = []
		# nbs = 0
		# x = 0
		# while(nbs < 15):
		# 	x = randint(0, 236)
		# 	if x not in self.nb_list:
		# 		self.nb_list.append(x)
		# 		nbs = nbs + 1
		# 	if len(self.nb_list_big > 225):
		# 		self.nb_list_big = []

		self.nb_list_small = []
		self.nb_list = img_creator.get_indices(3, self.nb_list_small)

		self.nb_list_big = []
		self.nb_list_big = img_creator.get_indices(15, self.nb_list_big)
		
		#self.imgwidget = ImgWidget()
		#self.img_choice_side = self.imgwidget.create_side(self.nb_list_big)

		#img choice big
		counter = 0
		i = 1
		j = 1
		self.img_choice_big = qtw.QWidget()
		self.img_choice_big.layout = qtw.QGridLayout()
		while (counter < 15):
			self.img = img_creator.get_img(img_path + self.list_img_files[self.nb_list_big[-counter]], 160)
			self.img_choice_big.layout.addWidget(self.img, i, j)
			i = i+1
			counter = counter + 1
			if i == 6 or i == 11:
				j = j + 1
				i = 1
			
		self.img_choice_big.setLayout(self.img_choice_big.layout)

		# #central widget
		self.central = qtw.QWidget()
		self.central.layout = qtw.QGridLayout()
		self.central.layout.addWidget(self.output, 0, 0, 3, 0)
		#self.central.layout.addWidget(self.img_choice, 2, 0)
		self.central.layout.addWidget(self.img_choice_big, 0, 2, 4, 1)
		#self.central.layout.addWidget(self.img_choice_side, 0, 2, 4, 1)
		self.central.setLayout(self.central.layout)
		self.setCentralWidget(self.central)

	
	#change img choice
	#right clicked
	def right_click(self):
		self.img01 = self.img02
		self.img02 = self.img03
		self.img03 = img_creator.get_img(img_path + self.list_img_files[randint(0, 235)])
		self.populate_widget()


	def left_click(self):
		self.img03 = self.img02
		self.img02 = self.img01
		self.img01 = img_creator.get_img(img_path + self.list_img_files[randint(0, 235)])
		print('otre')
	
	
	def clear_widget(self):
		#self.central.layout.removeWidget(self.img_choice)
		self.img_choice.close()

		# self.central.layout.removeWidget(self.img_choice)
		# sip.delete(self.img_choice)
		# self.img_choice = None

	def populate_widget(self):
		self.clear_widget()
		self.img_choice.layout.replaceWidget()
		self.img_choice.update()
		

	def create_img_choice(self):
		self.central = qtw.QWidget()
		self.central.layout = qtw.QGridLayout()
		self.central.layout.addWidget(self.output, 0, 0, 3, 0)
		self.central.layout.addWidget(self.img_choice, 2, 0)
		self.central.setLayout(self.central.layout)
		self.setCentralWidget(self.central)


	#grid: row, col, rowspan, colspan
	def create_img_choice_big(self):
		i = 0
		self.img_choice_big = qtw.QWidget()
		self.img_choice_big.layout = qtw.QGridLayout()
		while (i < 40):
			self.img = img_creator.get_img(img_path + self.list_img_files[randint(0, 236)])
			self.img_choice_big.layout.addWidget(self.img, i, 0)
			i = i+1
		self.img_choice_big.setLayout(self.img_choice_big.layout)

		



		

		
