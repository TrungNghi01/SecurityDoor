from LED_RGB import welcomeColor, warningColor, dangerColor, CorrectColor
from buzzer import buzzWelcome, buzzCorrect, buzzWrong, buzzDanger
from servoMotor import open_door, close_door
#from keypad import checkSpecialKeys, readLine
from time import sleep

def setup():
    print("Setting up the system")
    welcomeState()
    sleep(1)
    warningState()
    sleep(1)
    correctState()
    sleep(1)
    dangerState()


# def loop():
    # welcomeState()
    # if (checkSpecialKeys == True):
    #     correctState()
    # elif (checkSpecialKeys == False):
    #     for i in range(1, 5): 
    #         if (checkSpecialKeys() == True):
    #             correctState()
    #             break
    #         else:
    #             warningState() # just warning each time a wrong key is pressed
    #     else:
    #         dangerState() # after 5 wrong keys, danger state is activated


def welcomeState():
    print("welcomeState")
    welcomeColor()
    buzzWelcome()


def warningState():
    print("warningState")
    warningColor()
    buzzWrong()


def correctState():
    print("correctState")
    CorrectColor()
    buzzCorrect()
    open_door()
    sleep(5)
    close_door()


def dangerState():
    print("dangerState")
    dangerColor()
    buzzDanger()

setup()
