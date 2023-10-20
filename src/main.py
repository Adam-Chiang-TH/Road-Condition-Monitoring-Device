import snapshotter
import uploader

def init():
  snapshotter.init() # initialise camera
  uploader.init() # connect to server
  
def run():
    snapshotter.run()
    uploader.run()

def main():
  init()
  while True:
    run()

if __name__ == "__main__":
  main()
else:
  pass