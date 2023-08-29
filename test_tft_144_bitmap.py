# Test display of bitmap on TFT 1.44"

import board,busio
from time import sleep
from adafruit_st7735r import ST7735R
import displayio

# Set up pins
MOSI = board.GP11
SCLK = board.GP10
RESET = board.GP17
CS = board.GP13
DC = board.GP16

# The display is offset a little
# You may need to experiment with these values if you rotate the display
XOFFSET = 2
YOFFSET = 3

# Set up display as an SPI device
displayio.release_displays()
spi = busio.SPI(clock=SCLK, MOSI=MOSI)
display_bus = displayio.FourWire(spi, command=DC, chip_select=CS, reset=RESET)
display = ST7735R(display_bus, rotation=0, width=128+XOFFSET, height=128+YOFFSET, colstart=XOFFSET, rowstart=YOFFSET) 

# Setup the file as the bitmap data source
bitmap = displayio.OnDiskBitmap("/image.bmp")

# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)

# Loop forever so you can enjoy your image
while True:
    pass