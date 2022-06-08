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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#get list of filenames
		self.list_img_files = img_creator.get_file_list(img_path)

		#create list of numbers
		self.nb_list_small = []
		self.nb_list = img_creator.get_indices(3, self.nb_list_small)

		##create img choice widget
		self.img_widget = ImgWidget()
		self.img_choice_down = self.img_widget.create_img_widget(self.nb_list_small)

		#create btn
		self.btn_all = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_FileDialogListView),
										 '&', self)
		
		#create mirror area
		self.mirror = qtw.QLabel()
		self.mirror.setStyleSheet("background : lightblue")

		#create btn area
		self.btn_block = qtw.QWidget()
		self.btn_block.setStyleSheet("background : lightblue")
		self.btn_block.layout = qtw.QVBoxLayout()
		self.btn_block.layout.addWidget(self.btn_all)
		self.btn_block.layout.addStretch()
		self.btn_block.setLayout(self.btn_block.layout)

		#Create overall layout and assemble
		self.layout = qtw.QGridLayout()
		self.layout.addWidget(self.mirror, 0, 0, 4, 4)
		self.layout.addWidget(self.img_choice_down, 4, 0, 1, 5)
		self.layout.addWidget(self.btn_block, 0, 4, 4, 1)
		self.setLayout(self.layout)

		
	def update(self):
		self.clear()
		while i < 1:
			x = randint(0, 236)
			if x not in self.nb_list:
				self.nb_list.append(x)
				i = i+1
		self.img_choice_down = self.img_widget.create_img_widget(self.nb_list)
		self.img_widget.layout.addWidget(self.img_choice_down, 4, 0, 1, 5)
		self.setLayout(self.layout)


	def clear(self):
		sip.delete(self.img_choice_down)
		self.img_choice_down = None

			



