# Dependencies
import picamera

camera = picamera.PiCamera()
camera.vflip = True
camera.capture('image.jpg')
