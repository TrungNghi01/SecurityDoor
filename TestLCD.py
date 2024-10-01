#testing RGB LED
from gpiozero import RGBLED
from time import sleep

my_led = RGBLED(red=13, green=19, blue=26)

my_led.color = (1, 0, 0)  # all red
print("Red")
sleep(1)

my_led.color = (0, 1, 0)  # all green
print("Green")
sleep(1)

my_led.color = (0, 0, 1)  # all blue
print("Blue")
sleep(1)

my_led.color = (1, 1, 1)  # white
print("White")
sleep(1)
