from picamera2 import Picamera2
from PIL import Image
import time

def initCamAndGetSnapshot():
    camera = Picamera2()
    cameraConfig = camera.create_still_configuration()
    camera.configure(cameraConfig)
    camera.start()
    time.sleep(2)
    return camera.capture_image()

def main():
    img = initCamAndGetSnapshot()
    img.convert("L")
    img.save("a.jpg")
    pass

if __name__ == "__main__":
    main()
else:
    pass