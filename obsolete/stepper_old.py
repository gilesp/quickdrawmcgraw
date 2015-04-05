from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ControlPin = [7,8,9,10]

seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]]

def init():
    GPIO.setwarnings(False)
    for pin in ControlPin:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

def setStep(values):
    GPIO.output(ControlPin[0], values[0])
    GPIO.output(ControlPin[1], values[1])
    GPIO.output(ControlPin[2], values[2])
    GPIO.output(ControlPin[3], values[3])

def step(forwards, stepSize):
    if forwards:
        sequence = seq
    else:
        sequence = list(reversed(seq))
        
    for i in range(0,512):
        for step in range(0, 8, stepSize):
            for pin in range(0,4):
                GPIO.output(ControlPin[pin], sequence[step][pin])
            sleep(0.001 * stepSize)

init()

step(True, 1)

step(False, 1)

step(True, 2)

step(False, 2)


for pin in ControlPin:
    GPIO.output(pin, 0)
