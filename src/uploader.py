from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

from threading import Thread
from queue import Queue

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
folderName = "" # from logger, one folder level only no ('/')
folderDriveID = ""

queueImagesToUpload = Queue()

def worker():
  global drive, folderName, folderDriveID
  while True:
    filenameWithDir = queueImagesToUpload.get()  

    actualFilenameList = filenameWithDir.split('/')
    actualFilename = actualFilenameList[-1]

    file = drive.CreateFile({"title": actualFilenameList[-1], "parents": [{"id": folderDriveID}], "mimeType": "image/jpeg"})
    file.SetContentFile(filenameWithDir)
    file.Upload()

    threadWorker.run()

threadWorker = Thread(target = worker, daemon = True)

def init(name):
  global gauth, drive, folderName, folderDriveID
  gauth.LocalWebserverAuth()
  folderName = name

  folderMetadata = {'title' : folderName, 'mimeType' : 'application/vnd.google-apps.folder'}
  folder = drive.CreateFile(folderMetadata)
  folder.Upload()
  folderDriveID = folder['id']

def run(filenameWithDir):
  queueImagesToUpload.put(filenameWithDir)
  print(f"queueImagesToUpload.qsize() = {queueImagesToUpload.qsize()}")