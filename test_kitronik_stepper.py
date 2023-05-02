# Test stepper with kitronik robotics board

import PicoRobotics
import time


# Create robotics object
robot = PicoRobotics.KitronikPicoRobotics()

# Turn stepper 1 forward then backward
robot.step(1, "f", 50)
robot.step(1, "r", 50)

