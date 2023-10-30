from picamera2 import Picamera2
from PIL import Image

camera = Picamera2()

def init():
  global camera
  camera.resolution = (1280, 720)
  cameraConfig = camera.create_still_configuration()
  camera.configure(cameraConfig)
  camera.start()

def getImage():
  global camera
  return camera.capture_image()