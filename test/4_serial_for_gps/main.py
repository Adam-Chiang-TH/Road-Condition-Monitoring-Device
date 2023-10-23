import gps # comes with gpsd
import serial

port = "/dev/serial0" # serial0 for GPIO14 and GPIO15

def main():
  GPSPort = serial.Serial(port, baudrate = 9600, timeout = 0)
  while True:
    line = GPSPort.readline()
    #  print("A") # to test the blocking or non-blocking nature of readline()
    # Test conlusion of above: blocking or not depends on the timeout parameter (default is None which is blocking) of the serial object instantiation.
    if len(line) != 0:
        print(line)
        # print(line.decode("UTF-8"))

if __name__ == "__main__":
    main()
else:
    pass