import mv
import iot

def main():
  mv.init() # initialise camera
  iot.init() # connect to server
  while True:
    mv.run()
    iot.run()

if __name__ == '__main__':
  main()
else:
  pass