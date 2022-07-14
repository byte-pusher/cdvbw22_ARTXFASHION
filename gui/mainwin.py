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
from gui.sidechoiceview import SideChoice
from gui.final_view import FinalImg



class	MainWindow((qtw.QMainWindow)):
	"Main Window of Magic Mirror"

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setObjectName("main_window")
	
		#set basic window & geometry (SetGeometry> x,y, width, height)
		self.setWindowTitle("Magic Mirror")
		self.showMaximized()

		self.exitAction = qtg.QAction('&Neustart', self)
		self.exitAction.setShortcut(qtg.QKeySequence("Ctrl+e"))


		#create Widgets
		#choicewin
		self.sidebtns = SideBtns()
		self.sidebtns.choiceview()
		self.img_choice_bottom = ImgChoiceBottom()

		#modelview
		self.view = PyVistaView()
		self.modelview = self.view.plotter

		#final view
		self.final_img = FinalImg()

		#Grid arguments: row, column, rowSpan, columnSpan
		# overall layout init
		self.main_widget = qtw.QWidget()
		self.layout_main = qtw.QGridLayout()
		self.layout_main.addWidget(self.view.plotter, 0, 0, 160, 9)
		self.layout_main.addWidget(self.final_img, 135, 0, 25, 9)
		self.main_widget.setLayout(self.layout_main)
		self.setCentralWidget(self.main_widget)

		self.sidebtns.setStyleSheet("background-color : black")
		self.go_choiceview()

	# set esc key to end application
	def keyPressEvent(self, event):
		if event.key() == qtc.Qt.Key.Key_Escape:
			self.close()

	@qtc.pyqtSlot()
	def go_choiceview(self):
		self.sidebtns.choiceview()

		self.final_img.hide()
		self.layout_main.addWidget(self.img_choice_bottom, 125, 0, 35, 9)
		self.img_choice_bottom.setStyleSheet("background-color : black")
		self.img_choice_bottom.hide()
		self.img_choice_bottom.show()
		self.layout_main.addWidget(self.sidebtns, 0, 0, 10, 9)
		self.update()

	# @qtc.pyqtSlot()
	# def go_sidechoiceview(self):
	# 	self.layout_main.removeWidget(self.sidebtns)
	# 	self.layout_main.addWidget(self.sidebtns, 0, 5, 1, 1)
	# 	self.img_choice_bottom.hide()
	# 	self.final_img.hide()
	# 	self.load.hide()
	# 	self.img_choice_side.show()
	# 	self.update()

	@qtc.pyqtSlot()
	def go_finalview(self):
		self.sidebtns.finalview()
		self.img_choice_bottom.hide()
		self.final_img.show()
		self.img_choice_bottom.hide()
		self.update()

	@qtc.pyqtSlot()
	def go_wear(self):
		self.sidebtns.wear_view()
		self.update()


	#change to resizing 
	# @qtc.pyqtSlot()
	# def f_update(self):
	# 	self.update()
	# 	if self.winsize_status == 900:
	# 		self.resize(1200, 1800)
	# 		self.winsize_status = 901
	# 		print('update 901')
	# 	elif self.winsize_status == 901:
	# 		self.resize(1200, 1800)
	# 		self.winsize_status = 900
	# 		print('update 900')
	# 	else:
	# 		print('resizing error in f update')
	# 	self.showMaximized()




		


	


		

		



		

		
