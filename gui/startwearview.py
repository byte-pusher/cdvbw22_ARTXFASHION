#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/   


from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from path import icon_path

class	StartWear(qtw.QWidget):
	sig_end = qtc.pyqtSignal()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.countdown = qtw.QLabel()
		self.loading = qtg.QMovie(icon_path + 'countdown.gif')
		#source: https://gifer.com/de/8fWG
		self.countdown.setMovie(self.loading)
		self.main_layout = qtw.QGridLayout()
		self.main_layout.addWidget(self.countdown)
		self.setLayout(self.main_layout)
		self.loading.stop()
	
	def start_gif(self):
		self.loading.start()

	def stop_gif(self):
		self.loading.stop()
		self.countdown.hide()
		self.emit_end()
		#signal loadin ended emit

	def emit_end(self):
		self.sig_end.emit()