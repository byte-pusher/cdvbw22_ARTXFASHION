#  _____                           ________                 __  .__                  
 # /  |  |   _______  __ ___________\_____  \   ____   _____/  |_|  |__   ___________ 
 #/   |  |__/ __ \  \/ // __ \_  __ \/  ____/  / ___\_/ __ \   __\  |  \_/ __ \_  __ \
#/    ^   /\  ___/\   /\  ___/|  | \/       \ / /_/  >  ___/|  | |   Y  \  ___/|  | \/
#\____   |  \___  >\_/  \___  >__|  \_______ \\___  / \___  >__| |___|  /\___  >__|   
#     |__|      \/          \/              \/_____/      \/          \/     \/     



from random import randint
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import sip

from gui.pic_utils import img_creator

from path import img_path
img_path = img_path

class	SideChoice(qtw.QWidget):
	# signals for set up of finalview
	emit_img = qtc.pyqtSignal(str)
	emit_focus = qtc.pyqtSignal(str)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#get list of filenames
		self.list_img_files = img_creator.get_file_list(img_path)

		#create list of numbers
		self.nb_list = []
		self.nb_list = img_creator.get_indices(9, self.nb_list)

		#create img big area
		self.focus_img = qtw.QLabel()
	
		#get side choice
		self.overall_layout = qtw.QGridLayout()
		self.set_img_widget()
		#self.overall_layout.addWidget(self.img_choice_big, 7, 6, 9, 3)
		self.setLayout(self.overall_layout)
	

	#create img choice widget
	def set_img_widget(self):

		self.img_choice_big = qtw.QWidget()
		self.img_choice_big.setObjectName('img_choice_side')
		self.img_choice_big_layout = qtw.QGridLayout()
		
		#manual creation of img widgets to ensure connection
		self.focus_size = 160
		self.img1 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-1]], self.focus_size)
		self.img_choice_big_layout.addWidget(self.img1,0, 1)
		self.img1.mousePressEvent = self.emit1

		self.img2 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-2]], self.focus_size)
		self.img_choice_big_layout.addWidget(self.img2,1 ,1)
		self.img2.mousePressEvent = self.emit2

		self.img3 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-3]], self.focus_size)
		self.img_choice_big_layout.addWidget(self.img3,2 ,1)
		self.img3.mousePressEvent = self.emit3

		self.img4 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-4]], self.focus_size)
		self.img_choice_big_layout.addWidget(self.img4,0 ,2)
		self.img4.mousePressEvent = self.emit4

		self.img5 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-5]], self.focus_size)
		self.img_choice_big_layout.addWidget(self.img5,1 ,2)
		self.img5.mousePressEvent = self.emit5

		self.img6 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-6]], self.focus_size)
		self.img_choice_big_layout.addWidget(self.img6,2 ,2)
		self.img6.mousePressEvent = self.emit6

		self.img7 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-7]], self.focus_size)
		self.img_choice_big_layout.addWidget(self.img7,0 ,3)
		self.img7.mousePressEvent = self.emit7

		self.img8 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-8]], self.focus_size)
		self.img_choice_big_layout.addWidget(self.img8,1 ,3)
		self.img8.mousePressEvent = self.emit8

		self.img9 = img_creator.get_img_own(img_path + self.list_img_files[self.nb_list[-9]], self.focus_size)
		self.img_choice_big_layout.addWidget(self.img9,2 ,3)
		self.img9.mousePressEvent = self.emit9

		#set focus img to first of current selection
		self.set_focus_img(self.img1.name)

		#fill rest of layout
		self.img_choice_big.setLayout(self.img_choice_big_layout)

		self.overall_layout.addWidget(self.img_choice_big, 7, 6, 9, 3)
		self.setLayout(self.overall_layout)

		#ask for f update of main win
		self.sig_f_update.emit()

	#clear img_choice_big for new shuffle/turn
	def clear(self):
		self.img_choice_big.hide()
		self.overall_layout.removeWidget(self.img_choice_big)
		sip.delete(self.img_choice_big)
		self.img_choice_big = None

	#extend random choice list of images
	def extend_list(self):
		i = 0
		if len(self.nb_list) > 225:
			self.nb_list = []
		while (i < 9):
			x = randint(0, 233)
			if x not in self.nb_list:
				self.nb_list.append(x)
				i = i + 1
		print(self.nb_list)
			
	#turn to new site of images / create new random choice
	def turn(self):
		self.clear()
		self.extend_list()
		self.set_img_widget()
		self.setStyleSheet("background-color : transparent")

	# set current focus img as the one clicked
	@qtc.pyqtSlot(str)
	def set_focus_img(self, str_img):
		self.clear_focus()
		self.focus_holder = qtw.QLabel()
		self.focus_holder.setObjectName("focus_holder")
		self.focus_img  = img_creator.get_img_own(img_path + str_img, 400)
		self.focus_img.mousePressEvent = self.focus_emit
		self.focus_holder_layout = qtw.QGridLayout()
		self.focus_holder_layout.addWidget(self.focus_img, 1, 0, 3, 3)
		self.focus_holder.setLayout(self.focus_holder_layout)
		self.overall_layout.addWidget(self.focus_holder, 0, 6, 7, 3 )
		self.setLayout(self.overall_layout)
		self.update()

	#clear focus img widget
	def clear_focus(self):
		self.overall_layout.removeWidget(self.focus_img)
		sip.delete(self.focus_img)
		self.focus_img = None

	#focus emit for finalview
	def focus_emit(self, event):
		self.emit_focus.emit(self.focus_img.name)

	# emits for choosen imgs for focus
	def emit1(self, event):
		self.emit_img.emit(self.img1.name)

	def emit2(self, event):
		self.emit_img.emit(self.img2.name)

	def emit3(self, event):
		self.emit_img.emit(self.img3.name)

	def emit4(self, event):
		self.emit_img.emit(self.img4.name)

	def emit5(self, event):
		self.emit_img.emit(self.img5.name)

	def emit6(self, event):
		self.emit_img.emit(self.img6.name)

	def emit7(self, event):
		self.emit_img.emit(self.img7.name)

	def emit8(self, event):
		self.emit_img.emit(self.img8.name)

	def emit9(self, event):
		self.emit_img.emit(self.img9.name)

