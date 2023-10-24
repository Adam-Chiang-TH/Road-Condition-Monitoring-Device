# the whole sentence ends with \r\n

# append when len of readline is not 0

# import gps # comes with gpsd, useless for parsing(?)
import serial

port = "/dev/serial0" # serial0 for GPIO14 and GPIO15

STATE_PARSER_IDLE = 0 # wait for $
STATE_PARSER_STARTED = 1 # end at \r or \n
STATE_PARSER_COMPLETED = 2 # \r or \n detected, full sentence parsed

bufList = [""]
indexBuf = 0
stateParser = STATE_PARSER_IDLE

def updateParserState(char):
  global bufList, indexBuf, stateParser
  if char == '$' and stateParser == STATE_PARSER_IDLE:
    indexBuf = 0
    stateParser = STATE_PARSER_STARTED
  elif (char == '\r' or char == '\n') and stateParser == STATE_PARSER_STARTED:
    stateParser = STATE_PARSER_COMPLETED
  elif stateParser == STATE_PARSER_COMPLETED:
    indexBuf = 0
    bufList = [""]
    stateParser = STATE_PARSER_IDLE
  elif char == ',':
    indexBuf += 1
    bufList.append("")

def updateParserBuffer(char):
  global bufList, indexBuf
  if char != ',':
    bufList[indexBuf] += char

def main():
  global bufList, indexBuf, stateParser
  GPSPort = serial.Serial(port, baudrate = 9600, timeout = 0)
  
  while True:
    line = GPSPort.readline()
    for encodedChar in line: # this statement won't run at all if no line is read
      updateParserState(chr(encodedChar))

      if stateParser == STATE_PARSER_STARTED:
        updateParserBuffer(chr(encodedChar))
      elif stateParser == STATE_PARSER_COMPLETED:
        print(bufList)
        updateParserState(chr(encodedChar))
        pass


if __name__ == "__main__":
    main()
else:
    pass