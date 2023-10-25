from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
dirName = "testFolder" # from logger
folderDriveID = ""

def main():
  global gauth, dirName, folderDriveID
  gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

  drive = GoogleDrive(gauth)
  
  # From: https://github.com/googlearchive/PyDrive/issues/72#issuecomment-238947103
#   Create folder:
  folder_metadata = {'title' : 'TestFolder', 'mimeType' : 'application/vnd.google-apps.folder'}
  folder = drive.CreateFile(folder_metadata)
  folder.Upload()

#   Get folder info:
  folderid = folder['id']

  # From: https://stackoverflow.com/questions/30585166/create-a-folder-if-not-exists-on-google-drive-and-upload-a-file-to-it-using-py
  file1 = drive.CreateFile({'title': "Hello.txt", "parents": [{"id": folderid}], "mimeType": "application/vnd.google-apps.folder"})
  file1.Upload()

  fileImage = drive.CreateFile({'title': "inp.jpg", "parents": [{"id": folderid}], "mimeType": "image/jpeg"}) # https://copyprogramming.com/howto/python-pydrive-upload-to-specific-folder-not-own
  fileImage.SetContentFile("inp.jpg")
  fileImage.Upload()

if __name__ == "__main__":
  main()
else:
  pass

