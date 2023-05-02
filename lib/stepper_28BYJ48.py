# Class to drive the 28BYJ-48 stepper

import board
import digitalio
import time

#one hot encoding vectors
full_step_sequence = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

smooth_full_step_sequence = [
    [1,0,0,1],
    [1,0,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1]
]

# Stepper class
# Provide the GPIO pin numbers in1, in2, in3, in4
class Stepper:
    def __init__(self, in1, in2, in3, in4):

        self.pins = [
            digitalio.DigitalInOut(board.GP10),
            digitalio.DigitalInOut(board.GP11),
            digitalio.DigitalInOut(board.GP12),
            digitalio.DigitalInOut(board.GP13)]
        

        self.pins[0].direction = digitalio.Direction.OUTPUT
        self.pins[1].direction = digitalio.Direction.OUTPUT
        self.pins[2].direction = digitalio.Direction.OUTPUT
        self.pins[3].direction = digitalio.Direction.OUTPUT


    def forward(self, numSteps):
        for i in range(numSteps):
            for step in full_step_sequence:
                for i in range(len(self.pins)):
                    self.pins[i].value = step[i]
                    time.sleep(0.001)

    def backward(self, numSteps):
        for i in range(numSteps):
            for step in reversed(full_step_sequence):
                for i in range(len(self.pins)):
                    self.pins[i].value = step[i]
                    time.sleep(0.001)         

    def smoothForward(self, numSteps):
        for i in range(numSteps):
            for step in smooth_full_step_sequence:
                for i in range(len(self.pins)):
                    self.pins[i].value = step[i]
                    time.sleep(0.001)

    def smoothBackward(self, numSteps):
        for i in range(numSteps):
            for step in reversed(smooth_full_step_sequence):
                for i in range(len(self.pins)):
                    self.pins[i].value = step[i]
                    time.sleep(0.001)        
