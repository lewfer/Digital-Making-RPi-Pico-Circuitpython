# Test UDP server on wifi access point
#
# Make sure your settings.toml is empty
#

import wifi
import os
import ipaddress
import socketpool
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import time
import PicoRobotics
import board
import digitalio

# START WiFi access point
# ----------------------------------------------------------

# set access point credentials
ap_ssid = "MYSSID"
ap_password = "mypassword"

# Start access point
wifi.radio.start_ap(ssid=ap_ssid, password=ap_password)

# Show access point settings
print("Access point created with SSID: {}, password: {}".format(ap_ssid, ap_password))

# Show IP address
print("IP address is", wifi.radio.ipv4_address)


# START UDP server
# ----------------------------------------------------------

HOST = "192.168.4.1"  # see below
PORT = 5000
TIMEOUT = None
MAXBUF = 256

pool = socketpool.SocketPool(wifi.radio)

# Confirm IP address and self-ping
server_ipv4 = wifi.radio.ipv4_address_ap
print("Server IP address", server_ipv4)
print("Server ping", server_ipv4, wifi.radio.ping(server_ipv4), "ms")

print("Create UDP Server socket")
s = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
s.settimeout(TIMEOUT)

s.bind((HOST, PORT))

# Wait for messages
buf = bytearray(MAXBUF)
while True:
    print("Loop")
    size, addr = s.recvfrom_into(buf)
    print("Received", buf[:size], size, "bytes from", addr)


