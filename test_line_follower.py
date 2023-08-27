# Test line following sensors (3 way)

import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Set up the sensors on the 3 pins
right = DigitalInOut(board.GP6)
right.direction = Direction.INPUT
right.pull = Pull.DOWN   

middle = DigitalInOut(board.GP7)
middle.direction = Direction.INPUT
middle.pull = Pull.DOWN 

left = DigitalInOut(board.GP8)
left.direction = Direction.INPUT
left.pull = Pull.DOWN 

# Show the sensor status (True is light, False is dark)
while True:
    print(left.value, middle.value, right.value)
    time.sleep(0.01)