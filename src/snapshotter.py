from picamera2 import Picamera2

from PIL import Image

camera = Picamera2()

def init():
  global camera
  cameraConfig = camera.create_still_configuration({"size": (1280, 720)}) # do (1280, 720) for 720p
  camera.align_configuration(cameraConfig) # optimise size based on hardware
  print(cameraConfig["main"])
  camera.configure(cameraConfig)
  camera.start()
  
def getImage():
  
  global camera
  return camera.capture_image()