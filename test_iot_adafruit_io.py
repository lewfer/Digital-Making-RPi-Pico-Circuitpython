# Test Adafruit IO 
#
# In the lib directory, make sure you have:
# adafruit_requests.mpy
# adafruit_io
# adafruit_minimqtt

import os
import time
import ssl
import microcontroller
import board
import busio
import adafruit_requests
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError
import network

# Connect to wifi
net = network.Network()
net.connectWifi()

# Get Adafruit io credentials
aio_username = os.getenv('aio_username')
aio_key = os.getenv('aio_key')

# Initialize an Adafruit IO HTTP API object
pool = net.socketPool()
requests = adafruit_requests.Session(pool, ssl.create_default_context())
io = IO_HTTP(aio_username, aio_key, requests)
print("connected to io")

# Get or create a test feed
try:
    test_feed = io.get_feed("test")
except AdafruitIO_RequestError:
    test_feed = io.create_new_feed("test")

# Set up some dummy values
# Ultimately, these values will come from your sensor
data = [23,24,26,27,22,21,18]

# Send the data to Adafruit IO
for i in range(len(data)):
    try:
        # Get data value 
        value = data[i]
        print("Read value: ", value)
        
        # Send to Adafruit io
        io.send_data(test_feed["key"], value)
        time.sleep(1)

    # If any errors, reset Pico W
    except Exception as e:
        print("Error:\n", str(e))
        print("Resetting microcontroller in 10 seconds")
        time.sleep(10)
        microcontroller.reset()
    #  delay
    time.sleep(1)

