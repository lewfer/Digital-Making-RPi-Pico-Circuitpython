# Test PWM brightness control on an LED

import time
import board
import analogio
import pwmio

# Set up the LED on pin 13 as an analogue output pin
led = pwmio.PWMOut(board.GP13, frequency=1000)

# Loop forever adjusting the LED brightness in the range 0 (off) to 65535 (full on)
while True:
    for brightness in range(0,65535,1000):
        led.duty_cycle = brightness
        time.sleep(0.1)