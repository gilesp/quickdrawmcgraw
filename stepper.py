# This code is based on the public domain code written by Stephen C Phillips.
# http://blog.scphillips.com/2012/12/a-python-class-to-move-the-stepper-motor/
 
# It works on the Raspberry Pi computer with the standard Debian Wheezy OS and
# the 28BJY-48 stepper motor with ULN2003 control board.

from time import sleep
import RPi.GPIO as GPIO

class Motor(object):
    
    def __init__(self, pins):
        self.pins = pins
        self.degreesPerStep = 5.625 / 64
        self.stepsPerRevolution = int(360 / self.degreesPerStep)  # 4096
        self.stepAngle = 0

        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
            
        self._setRpm(10)

    def _setRpm(self, rpm):
        """ Set the speed in RPM """
        self._rpm = rpm
        # _delay is how long to wait between step signals
        self._delay = (60.0 / rpm) / self.stepsPerRevolution
        # Tune this to meet the motor's capabilities
        # 28BYJ-48 will skip steps if delay is too short
        if (self._delay < 0.0009):
            self._delay = 0.0009

    # This lambda allows setting of rpm as if it were an attribute
    # while maintaining the _delay value
    rpm = property(lambda self: self._rpm, _setRpm)

    def moveTo(self, angle):
        """Take the shortest route to a particular angle (degrees)."""
        # Make sure there is a 1:1 mapping between angle and stepper sequence
        targetAngle = 8 * (int(angle / self.degreesPerStep) / 8)
        steps = targetAngle - self.stepAngle
        steps = (steps % self.stepsPerRevolution)
        if steps > self.stepsPerRevolution / 2:
            steps -= self.stepsPerRevolution
            print "moving " + `steps` + " steps"
            self._anticlockwise(-steps / 8)
        else:
            print "moving " + `steps` + " steps"
            self._clockwise(steps / 8)
        self.stepAngle = targetAngle

    def _anticlockwise(self, steps):
        GPIO.output(self.pins[0], 0)
        GPIO.output(self.pins[1], 0)
        GPIO.output(self.pins[2], 0)
        GPIO.output(self.pins[3], 0)
        for i in range(steps):
            GPIO.output(self.pins[0], 0)
            sleep(self._delay)
            GPIO.output(self.pins[2], 1)
            sleep(self._delay)
            GPIO.output(self.pins[3], 0)
            sleep(self._delay)
            GPIO.output(self.pins[1], 1)
            sleep(self._delay)
            GPIO.output(self.pins[2], 0)
            sleep(self._delay)
            GPIO.output(self.pins[0], 1)
            sleep(self._delay)
            GPIO.output(self.pins[1], 0)
            sleep(self._delay)
            GPIO.output(self.pins[3], 1)
            sleep(self._delay)

    def _clockwise(self, steps):
        GPIO.output(self.pins[0], 0)
        GPIO.output(self.pins[1], 0)
        GPIO.output(self.pins[2], 0)
        GPIO.output(self.pins[3], 0)
        for i in range(steps):
            GPIO.output(self.pins[2], 0)
            sleep(self._delay)
            GPIO.output(self.pins[0], 1)
            sleep(self._delay)
            GPIO.output(self.pins[3], 0)
            sleep(self._delay)
            GPIO.output(self.pins[1], 1)
            sleep(self._delay)
            GPIO.output(self.pins[0], 0)
            sleep(self._delay)
            GPIO.output(self.pins[2], 1)
            sleep(self._delay)
            GPIO.output(self.pins[1], 0)
            sleep(self._delay)
            GPIO.output(self.pins[3], 1)
            sleep(self._delay)

        
    def release(self):
        for pin in self.pins:
            GPIO.output(pin, 0)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    m = Motor([7,8,9,10])
    m.rpm = 15
    print "Pause in seconds: " + `m._delay`
    #m.moveTo(90)
    #sleep(1)
    #m.moveTo(0)
    #sleep(1)
    #m.moveTo(-90)
    #sleep(1)
    #m.moveTo(-180)
    #sleep(1)
    m.moveTo(180)
    m.moveTo(360)
    sleep(1)
    m.moveTo(-45)
    sleep(1)
    m.moveTo(-90)
    sleep(1)
    m.moveTo(-135)
    sleep(1)
    m.moveTo(-180)
    sleep(1)
    m.moveTo(-225)
    sleep(1)
    m.moveTo(-270)
    sleep(1)
    m.moveTo(-315)
    sleep(1)
    m.moveTo(0)
    sleep(1)
    GPIO.cleanup()
