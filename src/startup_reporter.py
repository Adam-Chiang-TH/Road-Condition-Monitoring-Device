from gpiozero import Buzzer # https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer

pinBuzzer = 26 # GPIO26, see https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering

buzzerObject = Buzzer(pinBuzzer)

def buzzBuzz():
    global buzzerObject
    buzzerObject.beep(on_time = 1, off_time = 1)

def shutUp():
    global buzzerObject
    buzzerObject.off()