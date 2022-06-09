 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     


#activate venv: source .venv/bin/activate

import sys 

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc
from gui.mainwin import MainWindow


class	MainApp(qtw.QApplication):
	'"Build Application from classes and signals"'

	def __init__(self,argv):
		super().__init__(argv)

		#general default stle
		self.setStyle("Fusion")
		
		#set mainwindow
		self.main = MainWindow()
		self.main.setStyleSheet("background : black")

		#connections
		self.main.choicewin.emit_choice.connect(self.main.finalview.get_chosen_img)
		self.main.choicewin.emit_choice.connect(self.main.show_final_win)
		self.main.choicewin.btn_all.clicked.connect(self.main.show_side_choice)
		
		#max for Fullscreen
		#self.main.showMaximized()
		self.main.show()


if __name__=="__main__":
	app = MainApp(sys.argv)
	app.exec()
