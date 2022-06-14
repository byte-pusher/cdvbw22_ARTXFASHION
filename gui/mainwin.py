 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     




from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

from gui.choicewin import ChoiceWin
from gui.side_choice_win import SideChoiceWin
from gui.final_view import FinalViewWin

from graphics.modelview import MainWindow

class	MainWindow((qtw.QMainWindow)):
	"Main Window of Magic Mirror"
	 #sigs

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
		#set basic window & geometry (SetGeometry> x,y, width, height)
		self.setWindowTitle("Magic Mirror")
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

		#create Widgets
		self.choicewin = ChoiceWin()
		self.finalview = FinalViewWin()
		self.sidechoicewin = SideChoiceWin()
		
		
		#stacked widget
		self.central = qtw.QStackedWidget()
		self.central.addWidget(self.choicewin)
		self.central.addWidget(self.finalview)
		self.central.addWidget(self.sidechoicewin)
		self.central.setCurrentIndex(0)
		self.setCentralWidget(self.central)

	def keyPressEvent(self, event):
		if event.key() == qtc.Qt.Key.Key_Escape:
			self.close()

	#slots & fts for view change
	@qtc.pyqtSlot()
	def show_choice(self):
		self.central.setCurrentIndex(0)
	
	@qtc.pyqtSlot()
	def show_final_win(self):
		self.central.setCurrentIndex(1)

	@qtc.pyqtSlot()
	def show_side_choice(self):
		self.central.setCurrentIndex(2)



	


	


		

		



		

		
