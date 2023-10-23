from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()

def init():
  # pydrive.auth
  gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

def run():
  print("iot.run is run!")
  pass

# def run():
#   # pydrive.drive
#   drive = GoogleDrive(gauth)

#   file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
#   file1.SetContentString('Hello World!') # Set content of the file from given string.
#   file1.Upload()