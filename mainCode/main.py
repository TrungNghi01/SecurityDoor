from LED_RGB import welcomeColor, warningColor, dangerColor, CorrectColor
from buzzer import buzzWelcome, buzzCorrect, buzzWrong, buzzDanger
from servoMotor import open_door, close_door
from keypad import checkSpecialKeys, readLine, setAllLines
from time import sleep

def setup():
    print("Setting up the system")
    
def loop():
    welcomeState()
    if (checkSpecialKeys == True):
        correctState()
    elif (checkSpecialKeys == False):
        warningState()

def welcomeState():
    welcomeColor()
    buzzWelcome()
    return "someone go near the door!!"

def warningState():
    warningColor()
    buzzWrong()
    return "someone is trying to open the door!!"

def correctState():
    CorrectColor()
    buzzCorrect()
    open_door()
    sleep(5)
    close_door()
    return "Door is open"

