from picamera import PiCamera
from time import sleep
i = 1
camera = PiCamera()
camera.capture('/home/murphy/image' + str(i) + '.jpg')
