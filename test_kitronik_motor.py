# Test motor with kitronik robotics board

import PicoRobotics
import time

# Create robotics object
robot = PicoRobotics.KitronikPicoRobotics()


print("Forward")
for speed in range(0,100):
    robot.motorOn(1, "f", speed)
    time.sleep(0.1)


print("Reverse")
for speed in range(0,100):
    robot.motorOn(1, "r", speed)
    time.sleep(0.1)

print("Stop")
robot.motorOff(1)
