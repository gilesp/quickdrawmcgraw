from time import sleep
import stepper
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor1 = stepper.Motor([7,8,9,10])
motor1.rpm = 15

motor2 = stepper.Motor([17,18,22,23])
motor2.rpm = 15

motor1.moveTo(180)
motor1.release()

for angle in range(0, 361, 45):
    motor2.moveTo(angle)
    sleep(0.5)

GPIO.cleanup()
