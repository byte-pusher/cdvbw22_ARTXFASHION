#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#pyqt imports
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

#own imports
from graphics.modelview import GlWidget

class	FinalViewWin(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#create mirror area
		self.mirror = qtw.QLabel()
		self.mirror.setStyleSheet("background : lightblue")

		#createinfobox
		self.info = qtw.QLabel()
		self.info.setText("Artist:  \nTitle:  \nYear:")
		
		self.info.setStyleSheet("color : white;"
								"background-color : black")
		self.info.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
		# #other color approach for label:
		# col = qtw.QGraphicsColorizeEffect()
		# col.setColor(qtc.Qt.GlobalColor.darkGreen)
		# self.info.setGraphicsEffect(col)
		# self.info.setStyleSheet("background : lightblue")

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
		#self.overall_layout.addWidget(self.oglw,0 ,0 ,4 ,4 )
		self.overall_layout.addWidget(self.modelview,0 ,0 ,4 ,4)
		self.overall_layout.addWidget(self.info, 6, 1, 1, 1)
		self.overall_layout.addWidget(self.btn_back,6 ,3, 1,1)
		self.overall_layout.addWidget(self.btn_wear, 6, 2, 1, 1)

	#set model movements on keys (moved to mainwin)
	# def keyPressEvent(self, event):
	# 	if event.key() == qtc.Qt.Key.Key_Up:
	# 		self.oglw.spin_up()
	# 	if event.key() == qtc.Qt.Key.Key_Down:
	# 		self.oglw.spin_down()
	# 	if event.key() == qtc.Qt.Key.Key_Left:
	# 		self.oglw.spin_left()
	# 	if event.key() == qtc.Qt.Key.Key_Right:
	# 		self.oglw.spin_right()
	# 	if event.key() == qtc.Qt.Key.Key_Space:
	# 		self.oglw.spin_none()

	# set clicked img as widget
	@qtc.pyqtSlot(object)
	def get_chosen_img(self, img):
		self.img = img
		self.overall_layout.addWidget(self.img, 6, 0, 1, 1)
		self.setLayout(self.overall_layout)
		self.show()

