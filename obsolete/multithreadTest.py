from time import sleep
import threading
import stepper
import RPi.GPIO as GPIO

motor1Pins = [7, 8, 9, 10]
motor2Pins = [17, 18, 22, 23]

def moveMotor(pins, degrees):
    sleep(1)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    motor = stepper.Motor(pins)
    motor.rpm = 15
    motor.moveTo(degrees)

motor1Thread = threading.Thread(target = moveMotor, args=(motor1Pins, 45))
motor2Thread = threading.Thread(target = moveMotor, args=(motor2Pins, -45))

motor1Thread.start()
motor2Thread.start()
