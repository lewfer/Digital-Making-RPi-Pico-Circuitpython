# Test wifi access point
#
# Make sure your settings.toml is empty
#

import wifi

# set access point credentials
ap_ssid = "MYSSID"
ap_password = "mypassword"

wifi.radio.hostname = "RPiPico"

# Start access point
wifi.radio.start_ap(ssid=ap_ssid, password=ap_password)

# Show access point settings
print("Access point created with SSID: {}, password: {}".format(ap_ssid, ap_password))

# Show IP address
print("IP address is", wifi.radio.ipv4_address_ap)

