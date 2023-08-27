# API call test

# In lib:
# adafruit_requests.mpy

import os
import time
import ssl
import wifi
import socketpool
import adafruit_requests

# Connect to wifi
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

# Initialize an Adafruit IO HTTP API object
pool = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)

requests = adafruit_requests.Session(pool, ssl.create_default_context())

# Create an http connection to talk to api
http = adafruit_requests.Session(pool)
   
# Create a URL to write data
#url = "https://api.apilayer.com/exchangerates_data/latest?symbols=GBP%2CJPY&base=USD"
url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2000"

# Write data
#response = http.post(url,data={"field1":100,"field2":200,"field3":300})
#response = requests.request("GET",url,headers={"apikey", "iMQR4MUqrEzPuK3gg35yLyhl1c52L4s8"})
#response = requests.get(url, headers={"apikey":"iMQR4MUqrEzPuK3gg35yLyhl1c52L4s8"})
response = requests.get(url)
print(response.text)

# Close the connection
response.close()





