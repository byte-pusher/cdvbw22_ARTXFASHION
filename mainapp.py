 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     


import sys 
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from gui.mainwin import MainWindow

from gui.stylesheet import stylesheet

from metadata.load_data import df_input

from tracking.camera_thread import Webcam

class	MainApp(qtw.QApplication):
	'"main class for application"'

	def __init__(self,argv):
		super().__init__(argv)
		self.winsize_status = 900

		#general default stle
		self.setStyle("Fusion")
		
		#set mainwindow
		self.main = MainWindow()
		self.main.setStyleSheet(stylesheet)

		#connect buttons to viewchanges
		self.main.sidebtns.sig_back.connect(self.main.go_choiceview)

		self.main.exitAction.triggered.connect(self.exit)

		#Webcam
		self.cam = Webcam()
		self.cam.worker.angles.connect(self.main.view.updating)
		self.cam.worker.x_diff.connect(self.main.view.scale)
		self.cam.worker.x_diff_always.connect(self.main.view.move)
		self.cam.worker.frames.connect(self.main.view.frames)
		self.cam.worker.move.connect(self.main.view.move_up)

		#connect img clicked to finalview
		self.main.img_choice_bottom.emit_choice.connect(self.main.final_img.get_chosen_img)
		self.main.img_choice_bottom.emit_choice.connect(self.main.view.get_img)
		self.main.img_choice_bottom.emit_choice.connect(self.main.go_finalview)
		self.main.img_choice_bottom.emit_choice.connect(self.main.update)

		self.main.img_choice_bottom.btn_shuffle.clicked.connect(self.main.go_choiceview)

		#connect btn wear to actions
		self.main.sidebtns.sig_wear.connect(self.main.go_wear)

		self.main.sidebtns.sig_wear.connect(self.main.view.activate)

		#start show applicaiton
		self.main.show()
		

if __name__=="__main__":
	app = MainApp(sys.argv)
	app.exec()
