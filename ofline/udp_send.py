import socket

UDP_IP = "192.168.1.38"
UDP_PORT = 55056
#MESSAGE = "{\"seat_status\":[\"0\",\"1\"]}"

def randommsg():
	from random import randint
	import json
	b = json.load(open("seat.json"))
	seat_number = int(b["seat_number"])
	a = "{\"seat_status\":["
	for i in xrange(seat_number):
		a += ("\""+str(randint(0,1))+"\",")
	a = a[:-1]+"]}"
	return a

MESSAGE = randommsg()
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))