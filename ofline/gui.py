from PyQt4 import QtCore,QtGui
from math import ceil
from time import sleep
import sys
class Window(QtGui.QWidget):
	def __init__(self,n):
		self.app = QtGui.QApplication([])
		QtGui.QWidget.__init__(self)
		self.seat_number = n
		self.c = 10
		self.seat_status = []
		self.r = int(ceil(float(n)/float(self.c)))
		self.connect(self,QtCore.SIGNAL("changeseat"),self.place_chair)
		self.initGUI()
		self.showMaximized()
		
	def initGUI(self):	
		
		self.outer_layout = QtGui.QGridLayout(self)
		
		self.heading = QtGui.QLabel('Seating Arrangement')
		self.heading.setAlignment(QtCore.Qt.AlignCenter)
		self.heading.setStyleSheet("font-size:40px; background-color:#B3FFFF")
		self.top_layout = QtGui.QHBoxLayout()
		self.top_layout.addWidget(self.heading)
		
		self.mid_layout = QtGui.QGridLayout()
		self.label = QtGui.QLabel("R/C")
		self.mid_layout.addWidget(self.label,0,0)
		for i in xrange(self.c):
			self.labelc = QtGui.QLabel(str(1+i))
			self.mid_layout.addWidget(self.labelc,0,i+1)
		for i in xrange(self.r):
			self.labelr = QtGui.QLabel(chr(65+i))
			self.mid_layout.addWidget(self.labelr,2*i+1,0,2,1)
			
		#self.place_chair()
		
		self.bottom_widget = QtGui.QWidget(self)
		self.bottom_widget.setStyleSheet("background-color : blue;")
		self.bottom_layout = QtGui.QHBoxLayout()
		self.bottom_layout.addWidget(self.bottom_widget)
		
		self.outer_layout.addLayout(self.top_layout,0,0,1,1)
		self.outer_layout.addLayout(self.mid_layout,1,0,9,1)
		self.outer_layout.addLayout(self.bottom_layout,10,0,1,1)
		
	def place_chair(self,a):
		self.seat_status = a
		temp1 = self.seat_number
		for i in xrange(self.r):
			temp = 1
			while(temp <= self.c and temp1 > 0):
				self.pixmap = self.chair_status(self.seat_status[i*self.c+temp-1])
				label = QtGui.QLabel()
				label.setPixmap(self.pixmap)
				self.mid_layout.addWidget(label,2*i+1,temp)
				temp += 1
				temp1 -= 1
	def startGUI(self):
		sys.exit(self.app.exec_())
		
	def refresh_chair(self,a):
		self.emit(QtCore.SIGNAL("changeseat"),a)

	def chair_status(self,q):
		pixmap = QtGui.QPixmap("b.png")
		pixmap = pixmap.scaled(64, 64)
		mask = pixmap.createMaskFromColor(QtGui.QColor(0, 0, 0), 1)
		p = QtGui.QPainter(pixmap)
		if q==1:
			p.setPen(QtGui.QColor(255, 0, 0))
		elif q==2:
			p.setPen(QtGui.QColor(0, 0, 255))
		elif q==3:
			p.setPen(QtGui.QColor(0, 255, 0))
		p.drawPixmap(pixmap.rect(), mask, mask.rect())
		p.end()
		return pixmap
		
if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	a = [1,2,3,0,1,2,0,2,3,1]
	window = Window(sys.argv[1],a)
	window.showMaximized()
	sys.exit(app.exec_())