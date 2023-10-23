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
  logger.init("../log/" + folderName)

  camera = snapshotter.init()
  snapshotter.getImage(camera).save("../log/" + folderName + "/a.jpg") # TODO: del

  # pos = coord_tracker.waitForPos()
  # uploader.init()

  # while True:
  #   
  #   if time.time() - t1 >= 0.25:
  #     t1 = time.time()
  #     img = snapshotter.getImage(camera)

if __name__ == "__main__":
  main()
else:
  pass