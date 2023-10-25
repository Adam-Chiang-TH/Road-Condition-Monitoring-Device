import time

import coord_tracker
import snapshotter
import uploader
import logger
import startup_reporter

from PIL import Image # TODO: del

def waitForUnixEpoch():
  ret = 0
  while ret == 0:
    ret = time.time()
  return ret

def main():
  startup_reporter.buzzBuzz()
  t1 = waitForUnixEpoch()
  folderName = time.strftime("%Y-%m-%d_%H-%M-%S")
  logger.init("../log/" + time.strftime("%Y-%m-%d_%H-%M-%S"))

  snapshotter.init()

  latitudePrevious = ""
  longitudePrevious = ""
  # (latitudePrevious, longitudePrevious) = coord_tracker.waitForPos() # toggle comment this line if testing without coordinate
  uploader.init(folderName)

  startup_reporter.shutUp()
  while True:
    coord_tracker._debug_ParseAndPrint() # toggle comment this line to view raw GPS message
    (hasPos, latitude, longitude) = coord_tracker.getPos()
    if hasPos == True:
      latitudePrevious  = latitude
      longitudePrevious = longitude
    if time.time() - t1 >= 0.25:
      t1 = time.time()
      img = snapshotter.getImage()
      # filename = logger.logImage(img, "{:.2f}".format(t1)) # test: lacks coordinate info
      filename = logger.logImage(img, "{:.2f}".format(t1) + f"_{latitudePrevious}_{longitudePrevious}") # release: has coords
      uploader.run(filename)

if __name__ == "__main__":
  main()
else:
  pass