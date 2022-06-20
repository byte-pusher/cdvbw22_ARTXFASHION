 #  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/       


import os
from random import seed
from random import randint
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

from path import img_path

#own Labelclass to add name/path info
class OwnLabel(qtw.QLabel):
	def __init__(self, name):
		super().__init__()
		self.name = name
	

class img_creator(qtw.QWidget):
	emit_choice = qtc.pyqtSignal(object)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		dirpath = img_path
		self.filelist = self.get_file_list(dirpath)

	#get scaled img in own Label class with pixmap from path
	def get_img_own(filepath, scale):
		img = OwnLabel(filepath)
		img.name = os.path.basename(filepath)
		pixmap = qtg.QPixmap(filepath)
		img.setPixmap(pixmap.scaled(scale, scale, qtc.Qt.AspectRatioMode.KeepAspectRatio))
		img.setAlignment((qtc.Qt.AlignmentFlag.AlignCenter))
		return(img)

	#get list of art files in dir from img_path
	def get_file_list(dirpath):
		path = dirpath
		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
		img_without_data = ['sgs_arc_xxx_ah-1-ge-div-538-0001r_001_m.jpg', 'sgs_grs_klee_d-2005-681-6_001_s.jpg', 'sgs_grs_schwitters_d-1966-316-4_001_s.jpg']
		for img in img_without_data:
			files.remove(img)
		return(files)

	# create X indices
	def get_indices(nb, list):
		count = 0
		x = 0
		while(count < nb):
			x = randint(0, 236)
			if x not in list:
				list.append(x)
				count = count + 1
			if len(list) > 230:
				list = []
		return(list)



	



	



