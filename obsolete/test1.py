from stepper import Motor
from inversekinematics import Kinematics
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
motor1 = Motor([7,8,9,10])
motor2 = Motor([17,18,22,23])
motor1.rpm = 5
motor2.rpm = 5

kin = Kinematics(247, 285) #millimetres

(angle1, angle2) = kin.computeAngles(200, 100)

print "Moving 1 to " + str(angle1)
motor1.moveTo(-angle1)
print "Moving 2 to " + str(angle2)
#motor2.moveTo(180 - angle2)
motor2.moveTo(-angle2)
motor1.release()
motor2.release()
GPIO.cleanup()
