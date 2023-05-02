# Test neopixel

import board
import neopixel

# Set the number of pixels connected
num_pixels = 30

# Create the neopixel object
pixels = neopixel.NeoPixel(board.GP22, num_pixels)

# Set the broghtness level (from 0 to 1)
pixels.brightness = 1

# Set the colours of all pixels
pixels.fill((255, 0, 0))

# Set the colours of pixels individually
pixels[0] = (0,255,0) # green
pixels[1] = (0,0,255) # blue
pixels[2] = (255,255,255) # white
