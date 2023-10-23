import os
from PIL import Image

folderName = ""

def init(inpName):
  folderName = inpName
  os.mkdir(folderName)

def logImage():
  pass