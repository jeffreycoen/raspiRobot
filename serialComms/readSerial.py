#note, this code is for reading ultrasonic rangefinder reading from arduino by raspi
import serial
print("serial imported")
from time import sleep
print("sleep imported")
sleep(1)

print("sleep executed")
ser = serial.Serial('/dev/ttyACM0', 9600)

print("serial linked")

sleep(1)
while 1 :
	ser.readline()
	print(ser.readline())
