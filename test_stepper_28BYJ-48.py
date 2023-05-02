# Test the 28BYJ-48 stepper

import time
import board
import stepper_28BYJ48

# Create the stepper object
stepper = stepper_28BYJ48.Stepper(board.GP10, board.GP11, board.GP12, board.GP13)

# Move forwards and backwards
numSteps = 100
stepper.forward(numSteps)
stepper.backward(numSteps)
stepper.smoothForward(numSteps)
stepper.smoothBackward(numSteps)
