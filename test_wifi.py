# Test wifi
#
# Make sure your wifi credentials are set up in settings.toml:
#
# CIRCUITPY_WIFI_SSID="YOURWIFISSID"
# CIRCUITPY_WIFI_PASSWORD="YOURPASSWORD"
#

import network

# Create a network object
net = network.Network()

# Connect to the wifi
net.connectWifi()

#  Test network by pinging Google
ipv4 = network.ipaddress.ip_address("8.8.4.4")
pingTime = network.wifi.radio.ping(ipv4)
if pingTime!=None:
    print("Ping google.com: %f ms" % (pingTime*1000))
else:
    print("Could not ping Google")

