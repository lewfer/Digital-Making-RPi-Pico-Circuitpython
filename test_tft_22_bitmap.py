# Test display of bitmap on TFT 2.2"

import board,busio
import adafruit_ili9341
import displayio

# Set up pins
MOSI = board.GP11
SCLK = board.GP10
RESET = board.GP17
CS = board.GP13
DC = board.GP16

# Set up display as an SPI device
displayio.release_displays()
spi = busio.SPI(clock=SCLK, MOSI=MOSI)
display_bus = displayio.FourWire(spi, command=DC, chip_select=CS, reset=RESET)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240, rotation=0)

# Setup the file as the bitmap data source
bitmap = displayio.OnDiskBitmap("/blinka_320_240.bmp")

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