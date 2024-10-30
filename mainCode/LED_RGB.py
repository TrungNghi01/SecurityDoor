from gpiozero import RGBLED
from time import sleep

my_led = RGBLED(red=13, green=19, blue=26)

# when visitor go near the door
def welcomeColor():
    my_led.color = (1, 1, 1)  # white color 
    print("Welcome to the door")

# when visitor input the wrong password in the first 4 times
def warningColor():
    my_led.color = (1, 1, 0) # yellow color  
    sleep(0.5)
    my_led.color = (0, 0, 0) # turn off the light

# when visitor input the wrong password in the last time
def dangerColor():
        my_led.color = (1, 0, 0)  # red color
        sleep(0.5)
        my_led.color = (0, 0, 0) # turn off the light

# when visitor iput the right password
def CorrectColor():
    my_led.color = (0, 1, 0)  # green color
    