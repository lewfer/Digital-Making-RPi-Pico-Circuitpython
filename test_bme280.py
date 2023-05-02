# Test BME280 weather sensor

import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

# Create sensor object, using the GP4/GP5 I2C bus
i2c = busio.I2C(board.GP5, board.GP4)  # SCL, SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)

# Change this to match the location's pressure (hPa) at sea level
# This calibrates the altitude measurement to 1m accuracy
bme280.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    time.sleep(2)