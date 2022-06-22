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

from metadata.load_data import df_input

from tracking.camera_thread import Webcam

class	MainApp(qtw.QApplication):
	'"Build Application from classes and signals"'

	def __init__(self,argv):
		super().__init__(argv)

		#general default stle
		self.setStyle("Fusion")
		
		#set mainwindow
		self.main = MainWindow()
		self.main.setStyleSheet(stylesheet)

		#connect buttons to viewchanges
		self.main.sidebtns.sig_side.connect(self.main.go_sidechoiceview)
		self.main.sidebtns.sig_back.connect(self.main.go_choiceview)

		Webcam
		self.cam = Webcam()
		self.cam.worker.angles.connect(self.main.view.updating)
		self.cam.worker.x_diff.connect(self.main.view.scale)
		self.cam.worker.mid_point.connect(self.main.view.move)
		self.cam.worker.frames.connect(self.main.view.frames)

		#connect img clicked to finalview
		self.main.img_choice_bottom.emit_choice.connect(self.main.final_img.get_chosen_img)
		self.main.img_choice_bottom.emit_choice.connect(self.main.view.get_img)
		self.main.img_choice_bottom.emit_choice.connect(self.main.go_finalview)

		#img side img clicked -> set img as focus view
		self.main.img_choice_side.emit_focus.connect(self.main.img_choice_side.set_focus_img)
		
		# side shuffle ft to turn ft
		self.main.img_choice_side.sig_f_update.connect(self.main.f_update)
		self.main.sidebtns.btn_shuffle.clicked.connect(self.main.img_choice_side.turn)


		
		#start show applicaiton
		self.main.show()
		

if __name__=="__main__":
	app = MainApp(sys.argv)
	app.exec()
