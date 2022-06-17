#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt imports
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc

#own imports
from gui.pic_utils import img_creator
from path import img_path

#own imports
from graphics.modelview import GlWidget

class	FinalViewWin(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		#createinfobox
		self.info = qtw.QLabel()
		self.info.setText("Artist:  \nTitle:  \nYear:")
		
		self.info.setStyleSheet("color : white;"
								"background-color : black")
		self.info.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
		
		#create modelview
		self.modelview = GlWidget()

		#create btn
		self.btn_back = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_MediaSkipForward),
										 '&', self)
		self.btn_back.setGeometry(10, 10, 60, 40)
		self.btn_back.setStyleSheet("text-align : center; border-radius : 5; border : 1px solid white")
		self.btn_wear = qtw.QPushButton(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogApplyButton),
										 '&', self)
		self.btn_wear.setGeometry(10, 10, 60, 40)								 
		self.btn_wear.setStyleSheet("text-align : center; border-radius : 5; border : 1px solid white")

		#set layout
		self.overall_layout = qtw.QGridLayout()
		self.overall_layout.addWidget(self.modelview,0 ,0 ,15 ,9)
		self.overall_layout.addWidget(self.info, 13, 0, 3, 9)
		self.overall_layout.addWidget(self.btn_back, 6, 9, 1, 1)
		self.overall_layout.addWidget(self.btn_wear, 7, 9, 1, 1)

	# set clicked img as widget
	@qtc.pyqtSlot(str)
	def get_chosen_img(self, str_img):
		print("recieved", str_img)
		self.img = img_creator.get_img_own(img_path + str_img, 160)
		self.overall_layout.addWidget(self.img, 13, 0, 3, 1)
		self.setLayout(self.overall_layout)
		self.show()

	# ft to retrieve info for img from pd frame
	# alternative bind info to img objects
	def set_info(self, str_img):
		self.info.setText("Artist:  \nTitle:  \nYear:")

