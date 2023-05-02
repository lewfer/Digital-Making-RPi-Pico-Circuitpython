# Test PIR

import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Set up the button on pin 16 as a digital input pin
pir = DigitalInOut(board.GP16)
pir.direction = Direction.INPUT
pir.pull = Pull.DOWN            

# Wait for intruders
while True:
    if pir.value:
        print("Intruder!")
        while pir.value:
            pass
    print("Waiting")
    time.sleep(0.1)

