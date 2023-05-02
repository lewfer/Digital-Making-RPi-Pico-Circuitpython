# Test button input (button connected to 3V3)

import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Set up the button on pin 18 as a digital input pin
switch = DigitalInOut(board.GP18)
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN               # Pull down so button value is True when pressed

# Show the button status (True is pressed, False is not pressed)
while True:
    print(switch.value)
    time.sleep(0.01)