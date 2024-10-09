from LED_RGB import welcomeColor, warningColor, dangerColor, CorrectColor
from buzzer import buzzWelcome, buzzCorrect, buzzWrong, buzzDanger
from servoMotor import open_door, close_door
from time import sleep

def welcomeState():
    welcomeColor()
    buzzWelcome()
    return "someone go near the door!!"

# def warningState():
#     if 
#     warningColor()
#     buzzWrong()
#     return "wrong password"