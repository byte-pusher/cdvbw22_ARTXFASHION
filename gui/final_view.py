#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     


from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

class	FinalViewWin(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#create mirror area
		self.mirror = qtw.QLabel()
		self.mirror.setStyleSheet("background : lightblue")

		#createinfobox
		self.info = qtw.QLabel()
		self.info.setText("Artist:  \nTitle:  \nYear:")
		self.info.setStyleSheet("background : lightblue")
		self.info.setAlignment(qtc.Qt.AlignmentFlag.AlignBottom)

		#create btns

		#set layout
		self.overall_layout = qtw.QGridLayout()
		self.overall_layout.addWidget(self.mirror,0 ,0 ,4 ,4)
		self.overall_layout.addWidget(self.info, 5, 0, 1, 1)

	# set clicked img as widget
	@qtc.pyqtSlot(object)
	def get_chosen_img(self, img):
		self.img = img
		print(type(img))
		self.overall_layout.addWidget(self.img, 6, 0, 1, 1)
		self.setLayout(self.overall_layout)
		self.show()

