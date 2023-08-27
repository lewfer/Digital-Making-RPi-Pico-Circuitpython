# Test XY Joystick

import time
import board
import analogio

#  Set up axes on pins 27 and 28 as an analogue input pin
axis1 = analogio.AnalogIn(board.GP27_A1)
axis2 = analogio.AnalogIn(board.GP28_A2)

# Value will be 0 to 65535 (direction of increase/decrease depending on the order of black/red wires)
while True:
    val1 = axis1.value
    val2 = axis2.value
    print(val1,val2)
    time.sleep(.2)