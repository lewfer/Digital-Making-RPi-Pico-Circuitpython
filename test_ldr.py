# Test LDR (Light Dependent Resistor, sometimes called a photocell)

import time
import board
import analogio

#  Set up the LDR on pin 28 as an analogue input pin
photocell = analogio.AnalogIn(board.GP28_A2)

# Value will be 0 to 65535 (0 for bright, 65535 for dark or vice versa depending on the order of black/red wires)
while True:
    val = photocell.value
    print(val)
    time.sleep(.2)