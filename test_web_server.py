# Code adapted from here: https://learn.adafruit.com/pico-w-http-server-with-circuitpython/code-the-pico-w-http-server
# Requires HTTPServer library from here: https://github.com/adafruit/Adafruit_CircuitPython_HTTPServer


import os
import time
import ipaddress
import wifi
import socketpool
import microcontroller
from adafruit_httpserver import Server, Request, Response, GET, POST


#  Connect to network
print()
print("Connecting to WiFi")

#  Set static IP address
# ipv4 =  ipaddress.IPv4Address("192.168.1.42")
# netmask =  ipaddress.IPv4Address("255.255.255.0")
# gateway =  ipaddress.IPv4Address("192.168.1.1")
# wifi.radio.set_ipv4_address(ipv4=ipv4,netmask=netmask,gateway=gateway)

#  Connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected to WiFi")
pool = socketpool.SocketPool(wifi.radio)

# Create an HTTP server
server = Server(pool, "/static", debug=True)

#  Variables for HTML
font_family = "monospace"

#  the HTML script
#  setup as an f string
#  this way, can insert string variables from code.py directly
#  of note, use {{ and }} if something from html *actually* needs to be in brackets
#  i.e. CSS style formatting
def webpage():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-type" content="text/html;charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    html{{font-family: {font_family}; background-color: lightgrey;
    display:inline-block; margin: 0px auto; text-align: center;}}
      h1{{color: deeppink; width: 200; word-wrap: break-word; padding: 2vh; font-size: 35px;}}
      p{{font-size: 1.5rem; width: 200; word-wrap: break-word;}}
      .button{{font-family: {font_family};display: inline-block;
        background-color: black; border: none;
        border-radius: 4px; color: white; padding: 16px 40px;
        text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}}
      .input{{font-family: {font_family};display: inline-block;
        background-color: white; border: none;
        border-radius: 4px; color: black; padding: 16px 40px;
        text-decoration: none; font-size: 30px; margin: 2px;}}
      p.dotted {{margin: auto;  width: 75%; font-size: 25px; text-align: center;}}
    </style>
    </head>
    <body>
    <title>Pico W HTTP Server</title>
    <h1>Pico W HTTP Server</h1>
    <br>
    <p class="dotted">This is a Pico W running an HTTP server with CircuitPython.</p>
    <br>
    <form accept-charset="utf-8" method="POST">
    <input class="input" name="input_text"/><br/>
    <button class="button" name="press_me" value="ON" type="submit">PRESS ME</button></a></p></form>
    </body></html>
    """
    return html

#  Serve up the main page
@server.route("/", GET)
def base(request: Request): 
    #  serve the HTML f string
    #  with content type text/html
    return Response(request, f"{webpage()}", content_type='text/html')

#  Process the submitted for
@server.route("/", POST)
def buttonpress(request: Request):
    #  get the raw text
    body = request.body.decode("utf8")
    print(body)
    #  reload site
    return Response(request, f"{webpage()}", content_type='text/html')

print("starting server..")
# Startup the server
try:
    server.start(str(wifi.radio.ipv4_address))
    print("Listening on http://%s:80" % wifi.radio.ipv4_address)
#  if the server fails to begin, restart the pico w
except OSError:
    time.sleep(5)
    print("restarting..")
    microcontroller.reset()

# Wait for requests
while True:
    try:
        #  poll the server for incoming/outgoing requests
        server.poll()
    except Exception as e:
        print(e)
        continue
