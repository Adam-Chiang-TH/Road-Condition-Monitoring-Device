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
  
  ret = f"{dirName}/{countImage}_{name}.jpg"
  img.save(ret)
  countImage += 1
  return ret