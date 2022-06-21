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
	sig_side = qtc.pyqtSignal()
	sig_shuffle_side = qtc.pyqtSignal()
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#create buttons
		# btn left
		self.btn_left = qtw.QPushButton(self)
		self.btn_left.setObjectName("btn_arrow_left")
		self.btn_left.setIcon(qtg.QIcon(icon_path + 'arrow_left'))
		self.icon_size_side = qtc.QSize(60,60)
		self.btn_left.setMinimumSize(80,80)
		self.btn_left.setIconSize(self.icon_size_side)
		self.btn_left.clicked.connect(self.sidechoiceview)
		self.btn_left.clicked.connect(self.emit_sig_side)
		self.btn_left.hide()

		#btn right
		self.btn_right = qtw.QPushButton(self)
		self.btn_right.setObjectName("btn_right")
		self.btn_right.setIcon(qtg.QIcon(icon_path + 'arrow_right'))
		self.icon_size_back = qtc.QSize(60,60)
		self.btn_right.setMinimumSize(60,60)
		self.btn_right.setIconSize(self.icon_size_back)
		self.btn_right.hide()

		#shuffle button side
		self.btn_shuffle = qtw.QPushButton(self)
		self.btn_shuffle.setObjectName("btn_shuffle_side")
		self.btn_shuffle.setIcon(qtg.QIcon(icon_path + 'shuffle'))
		self.icon_size_shuffle= qtc.QSize(60,60)
		self.btn_shuffle.setMinimumSize(60,60)
		self.btn_shuffle.setIconSize(self.icon_size_shuffle)
		self.btn_shuffle.hide()

		#button wear
		self.btn_wear = qtw.QPushButton()
		self.btn_wear.setObjectName('btn_wear')
		self.btn_wear.setIcon(qtg.QIcon(icon_path + 'wear'))
		self.icon_size_wear = qtc.QSize(60,60)
		self.btn_wear.setMinimumSize(60,60)
		#self.btn_wear.clicked.connect(self.turn)
		self.btn_wear.hide()
	
		#create layout
		self.btnside_layout = qtw.QVBoxLayout()
		self.btnside_layout.addWidget(self.btn_right)
		self.btnside_layout.addWidget(self.btn_left)
		self.btnside_layout.addWidget(self.btn_shuffle)
		self.btnside_layout.addWidget(self.btn_wear)
		self.setLayout(self.btnside_layout)

	def emit_sig_side(self):
		self.sig_side.emit()
	
	def emit_back(self):
		self.sig_back.emit()

	# #open 
	def choiceview(self):
		try:
			self.btn_right.hide()
			self.btn_wear.hide()
		except:
			pass
		
		try:
			self.btn_left.show()
		except:
			pass
		
		# self.update()
		# self.setLayout(self.btnside_layout)
		# self.show()



	def sidechoiceview(self):
		try:
			self.btn_left.hide()
		except:
			pass

		try:
			self.btn_right.show()   #, 0, 0)
			self.btn_shuffle.show()   #, 12, 0)
		except:
			pass
		


	# def btnside_finalview(self):
	# 	try:
	# 		self.btnside_layout.removeWidget(self.btn_right)
	# 		self.btnside_layout.removeWidget(self.btn_shuffle)
	# 	except:
	# 		pass

	# 	try:
	# 		self.btnside_layout.addWidget(self.btn_right, 7, 0)
	# 		self.btnside_layout.addWidget(self.btn_wear)
	# 	except:
	# 		pass
	# 	self.btnside.update()
