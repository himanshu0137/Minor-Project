from gui import Window
import json
import serial
import threading
from time import sleep

data_file = open('seat.json')
seat_data = json.load(data_file)
n = int(seat_data["seat_number"])
A = map(int,seat_data["seat_status"])

class UDP:
	def __init__(self):
		self.port = serial.Serial("COM10", baudrate=9600,timeout = 2)
		sleep(3)
		self.class_v = None
		self.b = None
	def recvdata(self,cv):
		self.class_v = cv
		while True:
			data = self.port.read(200)
			if data != '':
				print "received message:", data
				self.b = data
				self.B_data()
			
	def B_data(self):
		merged_seat_status = []
		self.sensor_data = json.loads(self.b)
		B =  map(int,self.sensor_data["seat_status"])
		for i in xrange(n):
			merged_seat_status.append(A[i]<<1 | B[i])
		print A
		print B
		print merged_seat_status
		self.class_v.refresh_chair(merged_seat_status)
				
w = Window(n)
udp = UDP()
udp_data = threading.Thread(target=udp.recvdata,args=(w,))

udp_data.start()
w.startGUI()
udp_data.join()
data_file.close()