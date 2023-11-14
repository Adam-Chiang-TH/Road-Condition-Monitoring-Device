from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

from threading import Thread
from queue import Queue

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
folderName = "" # from logger, one folder level only no ('/')
folderDriveID = ""

queueImagesToUpload = Queue()

def _init():
  global gauth, drive, folderName, folderDriveID
  gauth.LocalWebserverAuth()

  folderMetadata = {'title' : folderName, 'mimeType' : 'application/vnd.google-apps.folder'}
  folder = drive.CreateFile(folderMetadata)
  folder.Upload()
  folderDriveID = folder['id']

def _worker():
  _init()

  global drive, folderName, folderDriveID
  while True:
    print("worker thread started!")
    filenameWithDir = queueImagesToUpload.get(block = True, timeout = None)  

    actualFilenameList = filenameWithDir.split('/')
    actualFilename = actualFilenameList[-1]

    file = drive.CreateFile({"title": actualFilename, "parents": [{"id": folderDriveID}], "mimeType": "image/jpeg"})
    file.SetContentFile(filenameWithDir)
    file.Upload()

threadWorker = Thread(target = _worker, daemon = True)

def init(name):
  global folderName
  folderName = name
  threadWorker.start() # see https://docs.python.org/3/library/threading.html#threading.Thread.start

def run(filenameWithDir):
  queueImagesToUpload.put(filenameWithDir)
  print(f"queueImagesToUpload.qsize() = {queueImagesToUpload.qsize()}")