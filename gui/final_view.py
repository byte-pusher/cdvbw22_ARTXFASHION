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


class	FinalViewWin(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		#create mirror area
		self.mirror = qtw.QLabel()
		self.mirror.setStyleSheet("background : lightblue")

		#createinfobox
		self.info = qtw.QLabel()
		self.info.setText("Artist:  Title:  Year:")

		self.overall_layout = qtw.QGridLayout()
		self.overall_layout.addWidget(self.mirror,0 ,0 ,4 ,4)
		self.overall_layout.addWidget(self.info, 6, 2, 1, 1)


	@qtc.pyqtSlot(object)
	def get_chosen_img(self, img):
		self.img = img
		print(type(img))
		self.overall_layout.addWidget(self.img, 6, 1, 1, 1)
		self.setLayout(self.overall_layout)
		self.show()

