 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     


#activate venv in vscode: source .venv/bin/activate
# necessary package: PyQt6
# run: python3 mainapp.py

import sys 
from PyQt6 import QtWidgets as qtw
from gui.mainwin import MainWindow

from gui.stylesheet import stylesheet

class	MainApp(qtw.QApplication):
	'"Build Application from classes and signals"'

	def __init__(self,argv):
		super().__init__(argv)

		#general default stle
		self.setStyle("Fusion")
		
		#set mainwindow
		self.main = MainWindow()
		
		

		self.main.setStyleSheet(stylesheet)
		
		#connections
		#connect menubar action
		self.main.exitAction.triggered.connect(self.main.close)
		#connection from basic choice win to finalwin
		self.main.choicewin.emit_choice.connect(self.main.finalview.get_chosen_img)
		self.main.choicewin.emit_choice.connect(self.main.show_final_win)
		#from sidechoice to final win
		self.main.sidechoicewin.emit_focus.connect(self.main.finalview.get_chosen_img)
		self.main.sidechoicewin.emit_focus.connect(self.main.show_final_win)
		# sidechoicewin img to focus img
		self.main.sidechoicewin.emit_img.connect(self.main.sidechoicewin.set_focus_img)
		# from basic choice view to side choice view
		self.main.choicewin.btn_side.clicked.connect(self.main.show_side_choice)
		# back from sidechoice to basi choice win
		self.main.sidechoicewin.btn_back.clicked.connect(self.main.show_choice)
		# back from finalview to basic choice win
		self.main.finalview.btn_back.clicked.connect(self.main.show_choice)
		
		#start?show applicaiton
		self.main.show()

if __name__=="__main__":
	app = MainApp(sys.argv)
	app.exec()
