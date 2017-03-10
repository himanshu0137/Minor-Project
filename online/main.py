from gui import Window
import json
import socket
import threading
from time import sleep

data_file = open('seat.json')                           #Seat purchased data 
seat_data = json.load(data_file)
n = int(seat_data["seat_number"])
A = map(int,seat_data["seat_status"])

class UDP:
	def __init__(self):
		self.UDP_IP = "0.0.0.0"
		self.UDP_PORT = 55056
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.sock.bind((self.UDP_IP, self.UDP_PORT))                              #open port 
		self.class_v = None
		self.b = None
	def recvdata(self,cv):
		self.class_v = cv
		while True:
			data, addr = self.sock.recvfrom(1024)
			if data != None:
				self.b = data
				self.B_data()
			#print "received message:", self.data
			
	def B_data(self):
		merged_seat_status = []
		self.sensor_data = json.loads(self.b)
		B =  map(int,self.sensor_data["seat_status"])                  #Seat Sensor data
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