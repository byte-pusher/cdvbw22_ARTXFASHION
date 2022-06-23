#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/   


from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from path import icon_path


class SideBtns(qtw.QWidget):
	sig_back = qtc.pyqtSignal()
	sig_wear = qtc.pyqtSignal()
	sig_start = qtc.pyqtSignal()
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#style
		self.setStyleSheet('background : transparent')

		#create buttons
		# btn left
		# self.btn_left = qtw.QPushButton(self)
		# self.btn_left.setObjectName("btn_arrow_left")
		# self.btn_left.setIcon(qtg.QIcon(icon_path + 'arrow_left'))
		# self.icon_size_side = qtc.QSize(60,60)
		# self.btn_left.setMinimumSize(80,80)
		# self.btn_left.setIconSize(self.icon_size_side)
		# self.btn_left.clicked.connect(self.emit_back)
		# self.btn_left.hide()

		#btn right
		self.btn_right = qtw.QPushButton(self)
		self.btn_right.setObjectName("btn_right")
		self.btn_right.setIcon(qtg.QIcon(icon_path + 'arrow_right'))
		self.icon_size_back = qtc.QSize(60,60)
		self.btn_right.setMinimumSize(60,60)
		self.btn_right.setIconSize(self.icon_size_back)
		self.btn_right.clicked.connect(self.emit_back)
		self.btn_right.hide()

		# #shuffle button side
		# self.btn_shuffle = qtw.QPushButton(self)
		# self.btn_shuffle.setObjectName("btn_shuffle_side")
		# self.btn_shuffle.setIcon(qtg.QIcon(icon_path + 'shuffle'))
		# self.icon_size_shuffle= qtc.QSize(60,60)
		# self.btn_shuffle.setMinimumSize(60,60)
		# self.btn_shuffle.setIconSize(self.icon_size_shuffle)
		# self.btn_shuffle.hide()

		#button wear
		self.btn_wear = qtw.QPushButton()
		self.btn_wear.setObjectName('btn_wear')
		self.btn_wear.setIcon(qtg.QIcon(icon_path + 'shirt'))
		self.icon_size_wear = qtc.QSize(60,60)
		self.btn_wear.setMinimumSize(80,80)
		self.btn_wear.setIconSize(self.icon_size_wear)
		self.btn_wear.clicked.connect(self.emit_wear)
		self.btn_wear.hide()
	
		#create layout
		self.btnside_layout = qtw.QVBoxLayout()
		self.btnside_layout.addWidget(self.btn_right)
		#self.btnside_layout.addWidget(self.btn_shuffle)
		self.btnside_layout.addWidget(self.btn_wear)
		self.setLayout(self.btnside_layout)

	#emIt fts pder button/signal
	def emit_back(self):
		self.sig_back.emit()
	
	def emit_wear(self):
		self.sig_wear.emit()
	
	#fts to set buttons per view
	def choiceview(self):
		self.btn_wear.hide()
		self.btn_right.hide()
	
	def finalview(self):
		self.btn_wear.show()
		self.btn_right.show()

	def wear_view(self):
		self.btn_wear.hide()
		
	
