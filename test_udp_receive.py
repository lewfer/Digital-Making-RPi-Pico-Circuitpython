# Test UDP receive
#

import network

PORT = 5000

# Connect to WIFI
net = network.Network()
net.connectWifi()

# Create receiver to listen for messages
net.createReceiver(PORT)

# Receive messages
message = ""
while message!="stop":
    message = net.receiveMessage()
    print("Received", message)

net.closeSocket()

