from random import randint
import sys
json_file = open("seat.json","w")
a = "{\"seat_number\":\"" + sys.argv[1] + "\",\"seat_status\":["
for i in xrange(int(sys.argv[1])):
		a += ("\""+str(randint(0,1))+"\",")
a = a[:-1]+"]}"
json_file.write(a)