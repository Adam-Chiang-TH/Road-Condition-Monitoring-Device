import os
from PIL import Image

dirName = ""
countImage = 0

def init(inpName):
  global dirName
  dirName = inpName
  os.mkdir(dirName)

def logImage(img, name):
  global countImage
  # img.save(dirName + "/" + countImage + name + ".jpg")
  img.save(f"{dirName}/{countImage}_{name}.jpg")
  countImage += 1