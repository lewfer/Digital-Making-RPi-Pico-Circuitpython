# Test wifi
#
# Make sure your wifi credentials are set up in settings.toml:
#
# CIRCUITPY_WIFI_SSID="YOURWIFISSID"
# CIRCUITPY_WIFI_PASSWORD="YOURPASSWORD"
#
# https://learn.adafruit.com/pico-w-wifi-with-circuitpython/pico-w-basic-wifi-test


import os
import ipaddress
import wifi
import socketpool
    
print()
print("Connecting to WiFi")

#  Connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected to WiFi")

pool = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)

#  pings Google
ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

