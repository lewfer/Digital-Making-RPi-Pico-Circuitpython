# 16x2 character LCD test

import board
import busio
import time
from lcd.lcd import LCD, CursorMode
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Set up LCD display
i2c = busio.I2C(board.GP5, board.GP4) # SCL, SDA
interface = I2CPCF8574Interface(i2c, 0x27)
lcd = LCD(interface, num_rows=2, num_cols=20)
lcd.set_cursor_mode(CursorMode.HIDE)
lcd.set_backlight(1)

# Single line
lcd.clear()
lcd.print("abcdefghijklmnop")
time.sleep(2)

# Double line
lcd.clear()
lcd.print("Line 1\nLine 2")
time.sleep(2)

# Position
lcd.clear()
lcd.set_cursor_pos(1, 4)
lcd.print("Here I am")
time.sleep(2)

