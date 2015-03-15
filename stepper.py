# This code is based on the public domain code written by Stephen C Phillips.
# http://blog.scphillips.com/2012/12/a-python-class-to-move-the-stepper-motor/
 
# It works on the Raspberry Pi computer with the standard Debian Wheezy OS and
# the 28BJY-48 stepper motor with ULN2003 control board.

from time import sleep
import RPi.GPIO as GPIO

class Motor(object):
    
    def __init__(self, pins, fullStepping = None):
        self.pins = pins
        self.degreesPerStep = 5.625 / 64
        self.stepsPerRevolution = int(360 / self.degreesPerStep)  # 4096
        self.stepAngle = 0

        # 1 for halfstepping, 2 for fullstepping
        if (fullStepping):
            self.seqStepSize = 2
        else:
            self.seqStepSize = 1

        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
            
        self._setRpm(10)

    def _setRpm(self, rpm):
        """ Set the speed in RPM """

        # Tune this to meet the motor's capabilities
        # 28BYJ-48 will skip steps if delay is too short
        if (self.seqStepSize == 1 and rpm > 16):
            rpm = 16
        elif (self.seqStepSize == 2 and rpm > 7):
            rpm = 7

        self._rpm = rpm
        # _delay is how long to wait between step signals
        self._delay = (60.0 / rpm) / self.stepsPerRevolution
        

    # This lambda allows setting of rpm as if it were an attribute
    # while maintaining the _delay value
    rpm = property(lambda self: self._rpm, _setRpm)

    # The clockwise and anticlockwise step sequence for 28BJY-48 stepper motors
    _cw_seq = [ [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1],
                [1,0,0,1]]

    _acw_seq = list(reversed(_cw_seq))

    def moveTo(self, angle):
        """Take the shortest route to a particular angle (degrees)."""
        # Make sure there is a 1:1 mapping between angle and stepper sequence
        targetAngle = 8 * (int(angle / self.degreesPerStep) / 8)
        steps = targetAngle - self.stepAngle
        steps = (steps % self.stepsPerRevolution)
        if steps > self.stepsPerRevolution / 2:
            steps -= self.stepsPerRevolution
            print "moving " + `steps` + " steps"
            self.rotate(-steps / 8, True)
        else:
            print "moving " + `steps` + " steps"
            self.rotate(steps / 8)
        self.stepAngle = targetAngle

    def rotate(self, steps, anticlockwise = None):
        sequence = self._cw_seq

        if (anticlockwise):
            sequence = self._acw_seq

        for i in range(steps):
            for position in range(0, 8, self.seqStepSize):
                for pin  in range(0, 4):
                    GPIO.output(self.pins[pin], sequence[position][pin])
                sleep(self._delay)

        
    def release(self):
        for pin in self.pins:
            GPIO.output(pin, 0)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    m = Motor([7,8,9,10])
    m.rpm = 16
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
    sleep(1)
    m.moveTo(1)
    GPIO.cleanup()
