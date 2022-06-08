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
		self.nb_list = img_creator.get_indices(15, self.nb_list)

		##create img choice widget
		self.img_widget = ImgWidgetBig()
		self.img_choice_side = self.img_widget.create_img_widget(self.nb_list)

		#create btn
		self.btn_all = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_FileDialogListView),
										 '&', self)

		#create mirror area
		self.mirror = qtw.QLabel()
		self.mirror.setStyleSheet("background : lightblue")

		#Create overall layout and assemble
		self.layout = qtw.QGridLayout()
		self.layout.addWidget(self.mirror, 0, 0, 6, 4)
		self.layout.addWidget(self.img_choice_side, 0, 5, 6, 1)
		self.setLayout(self.layout)
		

		#stack side choices
		self.sideviews = qtw.QWidget()
		self.sideviews.layout = qtw.QStackedLayout()

		#get nb of necessary views
		img_per_view = len(self.nb_list)
		views = 237 / img_per_view

		# create nb of view widgets for stack
		i = 0
		while i < views:
			self.img_choice = self.img_widget.create_img_widget(self.nb_list)
			self.sideviews.layout.addWidget(self.img_choice)
			i = i + 1
		
		self.sideviews.layout.setCurrentIndex(1)
		self.sideviews.setLayout(self.sideviews.layout)
		
		
	def update(self):
		

	