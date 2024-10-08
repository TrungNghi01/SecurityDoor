from gpiozero import Servo
from time import sleep
 
myGPIO=27

servo = Servo(myGPIO)
 
def open_door():
    servo.mid()

def close_door():
    servo.min()


  


