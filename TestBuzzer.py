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

while True:
    buzz(440, 1)  # A4 pitch (440 Hz) for 1 second
    sleep(1)
    buzz(880, 1)  # A5 pitch (880 Hz) for 1 second
    sleep(1)
