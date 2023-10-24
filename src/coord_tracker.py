# the whole sentence ends with \r\n

# append when len of readline is not 0

# import gps # comes with gpsd, useless for parsing(?)
import serial

port = "/dev/serial0" # serial0 for GPIO14 and GPIO15

STATE_PARSER_IDLE = 0 # wait for $
STATE_PARSER_STARTED = 1 # end at \r or \n
STATE_PARSER_COMPLETED = 2 # \r or \n detected, full sentence parsed

bufList = [""] # DON'T USE THIS FOR DECODING BECAUSE IT IS CLEARED IMMEDIATELY UPON PARSE COMPLETION!
bufLisPrevious = [] # to save previous list, current buf is cleared immediately upon completion, USE THIS FOR DECODING!
indexBuf = 0
stateParser = STATE_PARSER_IDLE

serialGPS = serial.Serial(port, baudrate = 9600, timeout = 0)

def updateParserState(char): # also clears buffer if appropriate
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

def runParser():
  global bufList, bufListPrevious, indexBuf, stateParser
  hasCompleted = False
  
  line = serialGPS.readline()
  for encodedChar in line: # this statement won't run at all if no line is read
    updateParserState(chr(encodedChar))

    if stateParser == STATE_PARSER_STARTED:
      updateParserBuffer(chr(encodedChar))
    elif stateParser == STATE_PARSER_COMPLETED:
      hasCompleted = True
      bufListPrevious = bufList
      updateParserState(chr(encodedChar)) # update again to not ignore the rest of the characters in line
  return hasCompleted

def getCoord():
  hasCoord = False
  longitude = 0.00
  latitude = 0.00

  if runParser():
    pass # decode here
  return (hasCoord, longitude, latitude)

def _debug_ParseAndPrint():
  global bufList, indexBuf, stateParser

  if runParser() == True:
    print(bufListPrevious)