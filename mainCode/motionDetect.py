from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(18)

def motion_function():
    # trigger the whole system
    print("Motion detected!")

def no_motion_function():
    # keep the system sleep
    print("No motion detected!")

pir.when_motion = motion_function
pir.when_no_motion = no_motion_function

pause()