from LED_RGB import welcomeColor, warningColor, dangerColor, CorrectColor
from buzzer import buzzWelcome, buzzCorrect, buzzWrong, buzzDanger
#from servoMotor import open_door, close_door
#from keypad import checkSpecialKeys, readLine
from time import sleep

def setup():
    print("Setting up the system")
    welcomeColor()
    sleep(1)


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
    welcomeColor()
    buzzWelcome()
    return "someone go near the door!!"

welcomeState()

# def warningState():
#     warningColor()
#     buzzWrong()
#     return "someone is trying to open the door!!"

# def correctState():
#     CorrectColor()
#     buzzCorrect()
#     open_door()
#     sleep(5)
#     close_door()
#     return "Door is open"

# def dangerState():
#     dangerColor()
#     buzzDanger()
#     return "someone is trying to open the door!!"

