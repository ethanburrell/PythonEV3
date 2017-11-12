import time
import struct
import sys
sys.path.append ('PATH OF CURRENT FOLDER')
from pylib import ports_to_int
from pylib import move_time
from pylib import motor_stop

# command to start motor on port A at speed 50 for 5 seconds, then stop it
start_motor = move_time(ports='a', power=50, time=5)
stop_motor = motor_stop(ports='abcd')

# send commands to EV3 via bluetooth
with open('/dev/tty.EV3-SerialPort', 'w+', 0) as bt:
	bt.write(start_motor[0])
	print "writing"
	time.sleep(start_motor[1])
	bt.write(stop_motor)
	n = 0
	incoming =[]
	while n < 10:
		incoming.append(bt.read())
		time.sleep(1)
		n = n+1
	print incoming
