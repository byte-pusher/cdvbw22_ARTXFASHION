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
from gui.img_widget import ImgWidget, ImgWidgetBig

from gui.pic_utils import img_creator

from gui.stylesheet import stylesheet

from gui.choicewin import ChoiceWin
from gui.side_choice_win import SideChoiceWin
from gui.final_view import FinalViewWin

img_path = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'

class	MainWindow((qtw.QMainWindow)):
	"Main Window of Magic Mirror"
	 #sigs

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	

		#set basic window & geometry
		self.setWindowTitle("Magic Mirror")
		#setGeometry> x,y, width, height
		self.setGeometry(0, 0, 900, 1600)

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

		self.list_img_files = img_creator.get_file_list(img_path)


		self.nb_list_small = []
		self.nb_list = img_creator.get_indices(3, self.nb_list_small)

		self.nb_list_big = []
		self.nb_list_big = img_creator.get_indices(15, self.nb_list_big)
		
		self.img_widget_big = ImgWidgetBig()
		self.img_choice_side = self.img_widget_big.create_img_widget(self.nb_list_big)

		self.img_widget = ImgWidget()
		self.img_choice_down = self.img_widget.create_img_widget(self.nb_list_small)

		self.utils = img_creator()


		#initial central widget
		# self.central = qtw.QWidget()
		# self.central.layout = qtw.QGridLayout()
		# # self.central.layout.addWidget(self.output, 0, 0, 3, 0)
		# # self.central.layout.addWidget(self.img_choice_down, 2, 0)
		# # self.central.layout.addWidget(self.img_choice_side, 0, 2, 4, 1)
		# # self.central.setLayout(self.central.layout)


		self.choicewin = ChoiceWin()
		self.finalview = FinalViewWin()
		#self.side_choice_win = SideChoiceWin()
		self.setCentralWidget(self.choicewin)
		##self.setCentralWidget(self.side_choice_win)


		# #test stacked layout in general
		# self.central = qtw.QWidget()
		# self.central.layout = qtw.QStackedLayout()
		# self.central.layout.addWidget(self.output)
		# self.central.layout.addWidget(self.img_choice_down)
		# self.central.layout.addWidget(self.img_choice_side)
		# self.central.layout.setCurrentIndex(2)
		# self.central.setLayout(self.central.layout)
		# self.setCentralWidget(self.central)
		# self.central.layout.setCurrentIndex(1)



	#change img choice
	#right clicked
	def right_click(self):
		self.img01 = self.img02
		self.img02 = self.img03
		self.img03 = img_creator.get_img(img_path + self.list_img_files[randint(0, 235)])
		self.populate_widget()

	


		

		



		

		
