from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

def buzz(frequency, duration):
    period = 1.0 / frequency
    cycles = int(duration * frequency)
    for _ in range(cycles):
        buzzer.on()
        sleep(period / 2)
        buzzer.off()
        sleep(period / 2)

# the visitor go near the door 
def buzzWelcome():
    buzz(880, 1)  
    sleep(0.5)
    buzz(440, 1)  

# the visitor input the right password
def buzzCorrect():
    buzz(880, 1)  
    sleep(1)

# the visitor input the wrong password in the first 4 times
def buzzWrong():
    buzz(700, 1) 
    sleep(1)

# the visitor input the wrong password in the last time
def buzzDanger():
    buzz(300, 1) 
    sleep(0.5)

