# Test button input (button connected to ground)

import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Set up the button on pin 18 as a digital input pin
switch = DigitalInOut(board.GP18)
switch.direction = Direction.INPUT
switch.pull = Pull.UP               # Pull up so button value is True when not pressed

# Show the button status (False is pressed, True is not pressed)
while True:
    print(switch.value)
    time.sleep(0.01)