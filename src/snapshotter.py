from picamera2 import Picamera2
from PIL import Image

def init():
  camera = Picamera2()
  cameraConfig = camera.create_still_configuration()
  camera.configure(cameraConfig)
  camera.start()
  return camera

def getImage(camera):
  return camera.capture_image()