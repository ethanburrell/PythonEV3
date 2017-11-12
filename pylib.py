import struct
import time
def ports_to_int(ports):
	sum = 0;
	for i in range(0, len(ports)):
		port = ports[i]
		if port == 'a':
			sum = sum + 1
		elif port == 'b':
			sum = sum + 2
		elif port == 'c':
			sum = sum + 4
		elif port == 'd':
			sum = sum + 8
		else:
			sum = sum
	return sum

# Send command to EV3 To move motor for a certain amount of time
def move_time(ports, power, time):
#move_time(ports='cb', power=75, time=5)
	ports = ports_to_int(ports)
	print ports
	print power
	print time
	print chr(ports)
	powerH = struct.pack('1B',power)
	portsH= struct.pack('1B',ports)
	comm_0 = '\x0C\x00\x00\x00\x00\x00\x00'
	comm_1 = '\xA4\x00'+portsH+ powerH +'\xA6\x00'+portsH
	comm = comm_0  + comm_1
	#command = [comm,"time.sleep(",time,")",'\x09\x00\x0F\x00\x80\x00\x00\xA3\x00\x0F\x00']
	command = [comm,time]
	return command

# Stops the motor immediately
def motor_stop(ports):
	port = ports_to_int(ports)
	portsH =struct.pack('1B',port)
	l0 = struct.pack('1B',0)
	l1 = struct.pack('1B',1)
	comm_0 = '\x09\x00\x01\x00\x00\x00\x00'
	comm_1 = '\xA3' + l0 + portsH + l1
	command = comm_0 + comm_1
	print struct.unpack('11B', command)
	return command
