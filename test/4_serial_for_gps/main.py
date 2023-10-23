import gps # comes with gpsd
import serial

port = "/dev/serial0" # serial0 for GPIO14 and GPIO15

def main():
  GPSPort = serial.Serial(port, baudrate = 9600)
  while True:
     line = GPSPort.readline()
     print(line)

if __name__ == "__main__":
    main()
else:
    pass