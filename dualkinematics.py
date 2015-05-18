from math import acos, atan, asin, sin, degrees, sqrt
from pythagoras import cosineRule, angleA

class Kinematics(object) :

    def __init__(self, m1x, m1y, m2x, m2y, l1, l2, r1, r2):
        self.m1x = float(m1x)
        self.m1y = float(m1y)
        self.m2x = float(m2x)
        self.m2y = float(m2y)
        self.l1 = float(l1)
        self.l2 = float(l2)
        self.r1 = float(r1)
        self.r2 = float(r2)

    def computeAngle(self, x, y, l1, l2):
        c = sqrt(x**2 + y**2)
        e = angleA(c, l2, l1)
        a = atan(y/x)
        b = angleA(l2, l1, c)
        return a+b

#    def computeAngle(self, x, y, l1, l2):
#        c = sqrt(x**2 + y**2)
#        e = cosineRule(l1, l2, c)
#        a = atan(y/x)
#        b = asin((sin(e)/c) * l1)
#        return a+b

    def computeAngles(self, x, y):
        offsetX = x - self.m1x
        motor1 = self.computeAngle(offsetX, y + (-self.m1y), self.l1, self.l2)
        diff = self.m2x - self.m1x
        motor2 = self.computeAngle(diff - offsetX, y + (-self.m2y), self.r1, self.r2)
        return (degrees(motor1), degrees(motor2))

    # Based on this diagram:
    # http://forums.reprap.org/file.php?185,file=18866,filename=wally_diagram2.png
    # More info here:
    # http://forum.conceptforge.org/viewtopic.php?f=7&t=184&sid=9642f5c924e64be15d224c51d4deb6f9

if __name__ == "__main__":
    k = Kinematics(66, -25,  159, -26, 111, 110, 114, 111)
    (angle1, angle2) = k.computeAngles(200, 100)
    print "angle1 = " + str(angle1)
    print "angle2 = " + str(angle2)
    print "offset angle1 = " + str(90 - angle1)
    print "offset angle2 = " + str(90 - angle2)
