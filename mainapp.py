 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     


#activate venv: source .venv/bin/activate

import sys 

from PyQt6 import QtWidgets as qtw
from gui.mainwin import MainWindow
from gui.pic_utils import img_creator
from gui.img_widget import ImgWidget

img_path = '/Users/rkoop/Documents/cdvbw22/Data_Staatsgalerie_Stuttgart/Bilder/'

class	MainApp(qtw.QApplication):
	'"Build Application from classes and signals"'

	def __init__(self,argv):
		super().__init__(argv)

		#general default stle
		self.setStyle("Fusion")

		self.main = MainWindow()
		self.main.setStyleSheet("background : black")
		self.main.btn_left.clicked.connect(self.main.left_click)
		self.main.btn_right.clicked.connect(self.main.right_click)

		self.main.show()
		#self.widgets = ImgWidget()
		#self.img_creator.create_all_img(img_path)

		

if __name__=="__main__":
	app = MainApp(sys.argv)
	app.exec()
