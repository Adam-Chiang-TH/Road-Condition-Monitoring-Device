import mv
import iot

def main():
  mv.init() # initialise camera
  iot.init() # connect to server
  while True:
    mv.run()
    iot.run()

    while True: # TODO: delete, it's here to test Python program flow
      pass # TODO: delete

if __name__ == '__main__':
  main()
else:
  pass