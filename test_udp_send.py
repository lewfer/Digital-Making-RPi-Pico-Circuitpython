# Test UDP send
#
import network
import time

print()
print("Connecting to WiFi")

# Edit host and port to match server
HOST = "192.168.1.150"
PORT = 5000
TIMEOUT = 5

# Connect to WIFI
net = network.Network()
net.connectWifi()

# Create sender to send messages
net.createSender(HOST, PORT)

net.sendMessage("Hello there")
time.sleep(0.1)
net.sendMessage("from another Pico!")
time.sleep(0.1)
net.sendMessage("stop")


net.closeSocket()



