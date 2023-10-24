from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
dirName = "" # from logger

def init(name):
  # pydrive.auth
  global gauth, dirName
  gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
  dirName = name

def run(filename):
  drive = GoogleDrive(gauth)

  actualFilenameList = filename.split('/')
  file = drive.CreateFile({"title": actualFilenameList[-1]})
  file.SetContentFile(filename)
  file.Upload()

# def run():
#   # pydrive.drive
#   drive = GoogleDrive(gauth)

#   file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
#   file1.SetContentString('Hello World!') # Set content of the file from given string.
#   file1.Upload()