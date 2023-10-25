from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
folderName = "" # from logger, one folder level only no ('/')
folderDriveID = ""

def init(name):
  global gauth, drive, folderName, folderDriveID
  gauth.LocalWebserverAuth()
  folderName = name

  folderMetadata = {'title' : folderName, 'mimeType' : 'application/vnd.google-apps.folder'}
  folder = drive.CreateFile(folderMetadata)
  folder.Upload()
  folderDriveID = folder['id']

def run(filenameWithDir):
  global drive, folderName, folderDriveID

  actualFilenameList = filenameWithDir.split('/')
  file = drive.CreateFile({"title": actualFilenameList[-1], "parents": [{"id": folderDriveID}], "mimeType": "image/jpeg"})
  file.SetContentFile(filenameWithDir)
  file.Upload()