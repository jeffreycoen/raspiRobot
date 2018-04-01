# Attach: SR-04 Range finder

from rrb3 import *
import time, random
import picamera

camera = picamera.PiCamera()

BATTERY_VOLTS = 9
MOTOR_VOLTS = 6
rr = RRB3(BATTERY_VOLTS, MOTOR_VOLTS)


try:
    while True:
        distance = rr.get_distance()
        print(distance)
        
        if (distance < 20):
			camera.capture(str(time.clock()) + 'image.jpg')
        
        time.sleep(1)
finally:
    print("Exiting")
    rr.cleanup()

camera.capture('image.jpg')
