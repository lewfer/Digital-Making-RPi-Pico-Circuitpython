# ThingSpeak iot test

# In lib:
# adafruit_requests.mpy

import os
import time
import ssl
import adafruit_requests
import network

# Connect to wifi
net = network.Network()
net.connectWifi()

# Get Adafruit io credentials
THINGSPEAK_WRITE_API_KEY = os.getenv('THINGSPEAK_WRITE_API_KEY')

# Initialize an Adafruit IO HTTP API object
pool = net.socketPool()
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# Create an http connection to talk to api
http = adafruit_requests.Session(pool)
   
# Create a URL to write data
url = "http://api.thingspeak.com/update?api_key=" + THINGSPEAK_WRITE_API_KEY

# Write data
response = http.post(url,data={"field1":100,"field2":200,"field3":300})

# Close the connection
response.close()



