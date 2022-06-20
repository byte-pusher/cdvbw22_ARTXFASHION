#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     


#pyqt imports
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import sip

#own imports
from gui.pic_utils import img_creator
from path import img_path

#own imports
from graphics.modelview import GlWidget
from graphics.fashionview import PyVistaView

from metadata.load_data import df_input

class	FinalViewWin(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		# set img to None for check
		self.img = None

		#createinfobox
		self.info = qtw.QLabel()
		self.info.setObjectName("infotext")
		self.info.setText("Artist:  \nTitle:  \nYear:")
		self.info.setAlignment(qtc.Qt.AlignmentFlag.AlignVCenter)
		
		#create modelview
		self.view = PyVistaView()
		self.modelview = self.view.plotter.interactor

		#create btn
		self.btn_back = qtw.QPushButton(self)
		self.btn_back.setObjectName("btn_back")
		self.btn_back.setIcon(qtg.QIcon('gui/icons/arrow_right'))
		#self.btn_back.setGeometry(0, 0, 800, 800)
		self.btn_back.setMinimumSize(100,100)
		self.icon_size = qtc.QSize(80,80)
		self.btn_back.setIconSize(self.icon_size)
		
		#set layout
		self.overall_layout = qtw.QGridLayout()
		self.overall_layout.addWidget(self.modelview,0 ,0 ,15 ,9)
		self.overall_layout.addWidget(self.info, 13, 4, 3, 1)
		self.overall_layout.addWidget(self.btn_back, 5, 9, 5, 2)
	

	# set clicked img as widget
	@qtc.pyqtSlot(str)
	def get_chosen_img(self, str_img):
		#remove potential previous im from choicewin
		if self.img != None:
			self.clear()
		print("recieved:", str_img)
		#info_str 
		self.info.setText("Künstler: " + df_input.at[ str_img ,'artist'] + "\nTitel: " + df_input.at[ str_img ,'titel'] +  "\nEnstehungszeit: " + df_input.at[ str_img ,'entstehungszeit'])
		self.info.setText(df_input.at[ str_img ,'titel']  + "\n" + df_input.at[ str_img ,'artist'] + "\n" + df_input.at[ str_img ,'entstehungszeit'])
		#self.overall_layout.addWidget(self.info, 13, 1, 3, 1)
		self.img = img_creator.get_img_own(img_path + str_img, 160)
		self.overall_layout.addWidget(self.img, 13, 2, 3, 1)
		self.setLayout(self.overall_layout)
		self.show()

	def clear(self):
		self.img.hide()
		self.overall_layout.removeWidget(self.img)
		sip.delete(self.img)
		self.img = None

		

