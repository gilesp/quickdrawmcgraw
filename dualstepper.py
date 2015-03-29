from time import sleep
import RPi.GPIO as GPIO
import sys

class Motor(object):
    
    def __init__(self, pins):
        self.pins = pins
        self.degreesPerStep = 5.625 / 64
        self.stepsPerRevolution = int(360 / self.degreesPerStep)  # 4096
        self.stepAngle = 0
        self.seqStepSize = 1

        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def release(self):
        for pin in self.pins:
            GPIO.output(pin, 0)

    cw_sequence = [[1,0,0,0],
                   [1,1,0,0],
                   [0,1,0,0],
                   [0,1,1,0],
                   [0,0,1,0],
                   [0,0,1,1],
                   [0,0,0,1],
                   [1,0,0,1]]

    acw_sequence = list(reversed(cw_sequence))


class MotorController(object):

    def __init__(self, motor1, motor2):
        self.motor1 = motor1
        self.motor2 = motor2
        self._setRpm(10)

    def _setRpm(self, rpm):
        """ Set the speed in RPM """

        # Tune this to meet the motor's capabilities
        # 28BYJ-48 will skip steps if delay is too short
        if (rpm > 16):
            rpm = 16

        self._rpm = rpm
        self._delay = (60.0 / rpm) / self.motor1.stepsPerRevolution

    # This lambda allows setting of rpm as if it were an attribute
    # while maintaining the _delay value
    rpm = property(lambda self: self._rpm, _setRpm)

    def _calcSteps(self, motor, angle):
        targetAngle = 8 * (int(angle / motor.degreesPerStep) / 8)
        steps = targetAngle - motor.stepAngle
        steps = (steps % motor.stepsPerRevolution)
        motor.stepAngle = targetAngle
        anticlockwise = self._isAntiClockwise(steps, motor.stepsPerRevolution)
        if (anticlockwise):
            steps -= motor.stepsPerRevolution
            steps = -steps
        return (steps, anticlockwise)

    def _isAntiClockwise(self, steps, stepsPerRevolution):
        return steps > stepsPerRevolution / 2

    def moveTo(self, angle1, angle2):
        """Take the shortest route to a particular angle (degrees)."""
        (steps1, motor1AC) = self._calcSteps(self.motor1, angle1)
        (steps2, motor2AC) = self._calcSteps(self.motor2, angle2)

        self.rotate(steps1, motor1AC, steps2, motor2AC)

    def rotate(self, steps1, motor1AC, steps2, motor2AC):
        steps1 = steps1 / 8
        steps2 = steps2 / 8

        seq1 = self.motor1.acw_sequence if motor1AC else self.motor1.cw_sequence
        seq2 = self.motor2.acw_sequence if motor2AC else self.motor2.cw_sequence

        for i in range(max(steps1, steps2)):
            for position in range(0, 8, 1):
                for pin in range(0, 4):
                    if (i <= steps1):
                        GPIO.output(self.motor1.pins[pin], seq1[position][pin])
                    if (i <= steps2):
                        GPIO.output(self.motor2.pins[pin], seq2[position][pin])
                    sleep(self._delay)


if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    m1 = Motor([17,18,22,23])
    m2 = Motor([7,8,9,10])

    m1.release()
    m2.release()
    controller = MotorController(m1, m2)
    controller.rpm = 15

    controller.moveTo(float(sys.argv[1]), float(sys.argv[2]))
    GPIO.cleanup()
