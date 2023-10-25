import time

import coord_tracker
import snapshotter
import uploader
import logger

from PIL import Image # TODO: del

def waitForUnixEpoch():
  ret = 0
  while ret == 0:
    ret = time.time()
  return ret

def main():
  t1 = waitForUnixEpoch()
  folderName = time.strftime("%Y-%m-%d_%H-%M-%S")
  logger.init("../log/" + time.strftime("%Y-%m-%d_%H-%M-%S"))

  snapshotter.init()

  # (latitude, longitude) = coord_tracker.waitForPos()
  uploader.init(folderName)

  while True:
    coord_tracker._debug_ParseAndPrint()
    
    if time.time() - t1 >= 0.25:
      t1 = time.time()
      img = snapshotter.getImage()
      filename = logger.logImage(img, "{:.2f}".format(t1))
      uploader.run(filename)

if __name__ == "__main__":
  main()
else:
  pass