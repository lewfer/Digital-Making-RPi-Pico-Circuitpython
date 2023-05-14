# Test UDP send
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

print("Connected to WiFi")

#  Prints MAC address 
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  Prints IP address 
print("My IP address is", wifi.radio.ipv4_address)


# Create UDP sender
# -------------------------------------------------------------

# edit host and port to match server
HOST = "192.168.1.118"
PORT = 5000
TIMEOUT = 5

# Create a socket pool to allow network comms
pool = socketpool.SocketPool(wifi.radio)

# Create a socket
print("\nCreate UDP Client Socket")
s = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
s.settimeout(TIMEOUT)

# Send data
size = s.sendto(b'Hello, world', (HOST, PORT))
print("Sent", size, "bytes")

s.close()

