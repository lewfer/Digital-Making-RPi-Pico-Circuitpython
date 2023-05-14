# Test UDP receive
#

import os
import wifi
import socketpool

print()
print("Connecting to WiFi")

# Connect to WIFI
# -------------------------------------------------------------

#  Connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected to WiFi...")

#  Prints MAC address 
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  Prints IP address 
print("My IP address is", wifi.radio.ipv4_address)


# Create UDP listener
# -------------------------------------------------------------

HOST = str(wifi.radio.ipv4_address)
PORT = 5000
TIMEOUT = None
MAXBUF = 256

# Create a socket pool to allow network comms
pool = socketpool.SocketPool(wifi.radio)

# Create socket bound to a port
print("\nCreate UDP Server socket")
s = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
s.settimeout(TIMEOUT)
s.bind((HOST, PORT))

# Receive messages
buf = bytearray(MAXBUF)
while True:
    size, addr = s.recvfrom_into(buf)
    print("Received", buf[:size], size, "bytes from", addr)
    
