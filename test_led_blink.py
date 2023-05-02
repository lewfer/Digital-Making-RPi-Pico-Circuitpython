# Test blinking of an LED

import time
import board
import digitalio

# Set up the LED on pin 13 as a digital output pin
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

# Loop forever, blinking the LED
while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)