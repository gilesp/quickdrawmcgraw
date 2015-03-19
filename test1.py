from stepper import Motor
from inversekinematics import Kinematics
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
motor1 = Motor([7,8,9,10])
motor2 = Motor([20,21,22,23])
motor1.rpm = 16
motor2.rpm = 16

kin = Kinematics(100, 100) #millimetres

(angle1, angle2) = kin.computeAngles(50, 50)

motor1.moveTo(angle1)
motor2.moveTo(180 - angle2)
