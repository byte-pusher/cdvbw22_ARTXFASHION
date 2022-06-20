 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     

#PyQt imports
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

#own imports
from gui.choiceview import ImgChoiceBottom
from graphics.fashionview import PyVistaView

from gui.sidebtns import SideBtns


class	MainWindow((qtw.QMainWindow)):
	"Main Window of Magic Mirror"

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setObjectName("main_window")
	
		#set basic window & geometry (SetGeometry> x,y, width, height)
		self.setWindowTitle("Magic Mirror")
		self.setGeometry(0, 0, 900, 1600)


		#create Widgets
		#choicewin
		self.sidebtns = SideBtns()
		self.sidebtns.btnside_choiceview()
		self.imgchoicebottom = ImgChoiceBottom()

		#modelview
		self.view = PyVistaView()
		self.modelview = self.view.plotter

		#Grid arguments: row, column, rowSpan, columnSpan
		#
		self.main_widget = qtw.QWidget()
		self.layout_main = qtw.QGridLayout()
		self.layout_main.addWidget(self.view.plotter, 1, 1, 13, 7)
		self.layout_main.addWidget(self.sidebtns, 0, 8, 1, 1)
		self.layout_main.addWidget(self.imgchoicebottom, 14, 0, 4, 9)
		
		self.main_widget.setLayout(self.layout_main)
		self.setCentralWidget(self.main_widget)

		self.imgchoicebottom.setStyleSheet("background-color : transparent")
		self.sidebtns.setStyleSheet("background-color : transparent")




	# set esc key to end application
	def keyPressEvent(self, event):
		if event.key() == qtc.Qt.Key.Key_Escape:
			self.close()

	# #slots & fts for view change
	# @qtc.pyqtSlot()
	# def show_choice(self):
	# 	#self.central.setCurrentIndex(0)

	# @qtc.pyqtSlot()
	# def show_final_win(self):
	# 	#self.central.setCurrentIndex(1)

	# @qtc.pyqtSlot()
	# def show_side_choice(self):
	# 	#self.central.setCurrentIndex(2)
		
	

	


	


		

		



		

		
