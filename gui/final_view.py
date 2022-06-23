#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     


#pyqt imports
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import sip

#own imports
from gui.pic_utils import img_creator
from path import img_path

#own imports
from graphics.modelview import GlWidget
from graphics.fashionview import PyVistaView

from metadata.load_data import df_input

class	FinalImg(qtw.QWidget):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		sig_f_update = qtc.pyqtSignal()

		# set img to None for check
		self.img = None

		#createinfobox
		self.info = qtw.QLabel()
		self.info.setObjectName("infotext")
		self.info.setText("Artist:  \nTitle:  \nYear:")
		self.info.setAlignment(qtc.Qt.AlignmentFlag.AlignVCenter)

		#set layout
		self.overall_layout = qtw.QGridLayout()
		self.overall_layout.addWidget(self.info,0,3)


	# set clicked img as widget
	@qtc.pyqtSlot(str)
	def get_chosen_img(self, str_img):
		if self.img != None:
			self.clear()
		print("recieved:", str_img)
		self.info.setText("Künstler: " + df_input.at[ str_img ,'artist'] + "\nTitel: " + df_input.at[ str_img ,'titel'] +  "\nEnstehungszeit: " + df_input.at[ str_img ,'entstehungszeit'])
		self.info.setText(df_input.at[ str_img ,'titel']  + "\n" + df_input.at[ str_img ,'artist'] + "\n" + df_input.at[ str_img ,'entstehungszeit'])
		self.img = img_creator.get_img_own(img_path + str_img, 160)
		self.overall_layout.addWidget(self.img,0,2)
		self.setLayout(self.overall_layout)

	def clear(self):
		self.img.hide()
		self.overall_layout.removeWidget(self.img)
		sip.delete(self.img)
		self.img = None

	

		

